# Sentiment Analysis System

A text classificaion system that classifies a given text as exhibiting **Positive** 
or **Negative** sentiment using machine learning and Natural Language Processing 
(NLP).

## Project Overview

The aim of this project was to develop a sentiment analysis and classification 
system capable of determining the sentiment exhibited by a piece of text. The 
project goes through the complete machine learning workflow, covering:

- Data exploration
- Data cleaning
- Exploratory Data Analysis (EDA)
- Text preprocessing
- TF-IDF feature engineering
- Train/validation/test splitting
- Machine learning model comparison
- Hyperparameter tuning
- Model evaluation

Additionally, a user friendly interface was developed using **streamlit** to 
make it easier to run user text through the model for classification.

## Dataset

The dataset used in this project was the **Sentiment140 dataset**, sourced from 
Kaggle. The dataset contains 1.6 million tweets labelled according to their sentiment 
with '0' representing negative and '1' representing positive sentiment.

The dataset was split into the training, validation, and test sets with a split 
of 70% Training, 15% Validation, and 15% Testing.

## Data Preprocessing

A custom function was defined for the purposes of cleaning the text remove 
unwanted features and lemmatize the text. The function performed the following: 

- Converting text to lowercase
- Removing URLs
- Removing user mentions
- Removing hashtag symbols
- Removing numbers
- Removing punctuation
- Removing unnecessary whitespace
- Removing English stopwords
- Lemmatization

This same function is used to process text entered into the final application.

## Exploratory Data Analysis

EDA was performed to understand the structure and distribution of the dataset. 
The analysis included:

- Sentiment class distribution
- Text length analysis
- Common words
- Distribution of tweet lengths
- Examination of cleaned text

## Feature Engineering

As text cannot be directly provided to a machine learninig algorithm  the cleaned 
text was converted into numerical features using the **TF-IDF** vectorizer. 
The TFIDF vectorizer was fitted only on the training data to prevent data leakage 
and the validation and test data were transformed using the already fitted vector.

## Machine Learning Models

We explored four machine learning classifiers, namely:

1. Multinomial Naive Bayes
2. Logistic Regression
3. Linear Support Vector Machine
4. Random Forest

The models were evaluated using the measures of:

- Accuracy
- Precision
- Recall
- F1-score

### Model Comparison

| Model | Accuracy | Precision | Recall | F1 Score |
|---|---:|---:|---:|---:|
| Naive Bayes | 76.29% | 76.30% | 76.29% | 76.29% |
| Logistic Regression | 77.72% | 77.77% | 77.72% | 77.70% |
| Linear SVM | 77.65% | 77.73% | 77.65% | 77.63% |
| Random Forest | 76.80% | 76.80% | 76.80% | 76.80% |

## Model Selection

Logistic Regression achieved the best validation performance among the models 
tested. Hyperparameter tuning was subsequently performed using `GridSearchCV`.
The main hyperparameter investigated was:

C,

and the best value identified during cross-validation was:

C = 1.

## Hyperparameter Tuning

After performing hyperparameter tuning, the final model was evaluated on the 
previously untouched test set. 

| Metric | Score |
|---|---|
| Accuracy | 77.79% |
| Precision | 77.84% |
| Recall | 77.79% |
| F1 Score | 77.78% |

## Application

The trained logistic regression model was deployed through a **streamlit web application**.
The application takes user text, runs the text through the preprocessor, analyses 
the text, makes a positive or negative prediction, and displays the model's 
confidence level. The process goes as follows:

**Input:**

"I absolutely love machine learning."

**Output:**

Sentiment: Positive
Confidence: 96.24%

--------------------

## Installation

Clone the repository using:

    git clone https://github.com/MahlaselaLetsoalo/sentiment-analysis-app.git

Navigate to the project using:

    cd "Sentiment Analysis System"

Install the required dependencies

    python -m pip install -r requirements.txt

## Running the Application

From the project's root folder, run:

    python -m streamlit run App/app.py

--------------------

**Mahlasela Peter Letsoalo**,
Computer Science Graduate

Hope you have nothing but positive sentiments about the project 😁.