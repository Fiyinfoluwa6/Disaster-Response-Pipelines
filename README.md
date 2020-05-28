# Disaster-Response-Pipelines

## Table of Contents
1. Motivation
2. Project Summary
3. File Description
4. Installation
5. Instructions
6. License and Acknowledgement

## Motivation

Following a disaster, many disaster organizations get millions of messages either direct or via social media. Due to the volumes of these messages, many organiztions find it hard to manually pull our or filter this messages which are of importance to them. But with the help of machine learning, we are able to come up with a supervised learning approach to help organizations tackle this problem so that they can make betters decsions is disater situations.

## Project Summary
The intention of this project is to analyse a disaster dataset prepared and provided by figure Eight and and futher build a classifier model that is able to classify these disaster messages which is then integrated into an API for use.
The project is divided in three different sections:

* Extract, Transform and Load (ETL) : a pipeline was developed to extract data from a csv file, then we went furthert ot preproecss the data and load into a Sqllite Datas

* Machine Learning Pipelines : a pipeline was developed to apply natural language processing techniques to text for prepreprocessing and further use Ml algorith to classify them into there respective catgories

* Deployment : Lastly we deployed the model into a Cloud application platform in form of a Web App to use for predicting the messages

## File Discription
1. A Readme:md file
2. App folder: containing the files to run the application.
    * A python script to run the wep app(run.py)
    * Template file containing two html files(go.html,master.html) 

3. Data Folder: The folder containing the datasets use for the project, a script that does the preprocssing adn also generate a Sql db
    * DisasterResponse.db - SQLlite database of combined message data and categories.
    * disaster_categories.csv - The csv file containing the disaster categories.
    * disaster_messages.csv - The csv file containing the disaster messages.
    * process_data.py - Script that cleans and stores the data in a database.

4. Models Folder:The folder containing the scripts of the model and the saved model.

    * classifer.pkl: this file is the output of running train_classify.py.
    * train_classify.py: The python script to train the model and build the machine learning classifier model.

## Installations
The following libraries will be installed using Pip with Python 3.7 to run the files
   * NLTK
   * SQLAlchemy
   * Flask
   * Plotly
   
## Instructions

1. Run the following commands in the project's root directory to set up your database and mode
    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/

## License and Aknowledgement 
Sending profound regards to the entire team of [udacity](https://www.udacity.com/) for making this project availale and [figure8](https://figure-eight.com) for providing the dataset for use
