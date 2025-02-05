import sys
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os 
import nltk
import re
import pickle
import joblib
nltk.download(['punkt','wordnet', 'stopwords'])
import warnings
warnings.filterwarnings("ignore")
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, f1_score, precision_recall_curve, accuracy_score
from sklearn.multioutput import MultiOutputClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer

def load_data(database_filepath):
    """
    load the table from the disasterResponse.db
    
    Args:
        database_filepath :
    returns: target X and Y
    
    """
    engine = create_engine('sqlite:///{}'.format(database_filepath))
    df = pd.read_sql('df', engine)
    # extract values from X and y
    X =  df['message'].values
    Y = df.iloc[:, 4:].values
    category_names = list(df.columns[4:])
    return X, Y, category_names
  


def tokenize(text):
    """
    Args:
        text:
        
    Return:
        clean_tokens
    
    """
    text = re.sub(r'[^A-Za-z0-9]'," ",text.lower())
    text = word_tokenize(text)
    words = [w.strip() for w in text if w not in stopwords.words("english")]
    lemmatizer = WordNetLemmatizer()
    clean_tokens = [WordNetLemmatizer().lemmatize(w) for w in words]
    
    return clean_tokens
   

def build_model():
    
    """
    pipeline
    
    """
    pipeline = Pipeline([('CountVect',CountVectorizer(tokenizer=tokenize)),
                     ('Tfidf',TfidfTransformer()),
                     ('MultiClass',MultiOutputClassifier(OneVsRestClassifier(LinearSVC())))])
    
    
    parameters = {'CountVect__binary': [False,True],
              'Tfidf__norm': ['l1','l2'],
             'MultiClass__estimator__estimator__C': [1.0,3.0]
             }
    cv = GridSearchCV(pipeline,param_grid=parameters)
    return cv
  


def evaluate_model(model, X_test, Y_test, category_names):
    y_pred = model.predict(X_test)
    for idx,val in enumerate(category_names):
        print("Category:", val,"\n", classification_report(Y_test[:, idx], y_pred[:,idx]))
 


def save_model(model, model_filepath):
    joblib.dump(model, model_filepath)
  


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()