# FUTURE_ML_02
# Support Ticket Classification & Prioritization System

## Overview

This project is an end-to-end Natural Language Processing (NLP) and Machine Learning solution that automatically classifies customer support tickets and predicts their priority level.

The system helps support teams reduce manual ticket sorting, improve response times, and ensure urgent issues are handled quickly.

The application includes trained machine learning models, an interactive Streamlit dashboard, and a complete NLP preprocessing pipeline.


## Business Problem

Customer support teams often receive hundreds or thousands of tickets every day. Manually reviewing and routing these tickets is time-consuming and can lead to delays in resolving critical issues.

This project addresses these challenges by:

- Automatically categorizing support tickets
- Predicting ticket urgency levels
- Reducing manual workload
- Improving operational efficiency
- Enhancing customer satisfaction


## Project Objectives

The system automatically:

1. Reads customer support ticket text
2. Classifies tickets into predefined categories
3. Predicts ticket priority levels
4. Provides instant results through an interactive dashboard


## Dataset

**Dataset:** Customer Support Ticket Dataset

The dataset contains customer support records including:

- Ticket Subject
- Ticket Description
- Ticket Type
- Ticket Priority
- Ticket Status
- Customer Information

For this project, the Ticket Subject and Ticket Description fields were combined to create the text input used for training.


## Technologies Used

### Programming Language

- Python

### Data Processing

- Pandas
- NumPy

### Natural Language Processing

- NLTK
- spaCy

### Machine Learning

- Scikit-learn

### Feature Engineering

- TF-IDF Vectorization

### Model

- Multinomial Naive Bayes

### Deployment

- Streamlit



## Project Workflow

### 1. Data Preparation

- Loaded the dataset
- Inspected data quality and structure
- Combined Ticket Subject and Ticket Description into a single text feature

### 2. Text Preprocessing

The text data was cleaned using NLP techniques:

- Lowercasing
- Tokenization
- Stopword removal
- Lemmatization using spaCy

### 3. Feature Extraction

Text was converted into numerical features using:

- TF-IDF Vectorization
- Unigrams and Bigrams

### 4. Model Training

Two separate machine learning models were trained:

#### Ticket Type Classifier

Predicts categories such as:

- Billing Inquiry
- Technical Issue
- Product Inquiry
- Refund Request
- Cancellation Request

#### Priority Predictor

Predicts:

- Low
- Medium
- High
- Critical

### 5. Evaluation

Models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix


## Results

The project successfully demonstrates an end-to-end NLP workflow for support ticket automation.

### Key Outcomes

- Automated support ticket classification
- Automated ticket priority prediction
- Interactive Streamlit dashboard deployment
- TF-IDF feature engineering for text representation
- Machine learning model evaluation using classification metrics

### Business Impact

- Reduces manual ticket sorting effort
- Improves ticket routing efficiency
- Helps prioritize urgent customer issues
- Supports faster response times
- Enhances overall customer support operations


## Streamlit Dashboard

The project includes an interactive Streamlit dashboard that simulates a real-world support operations tool.

### Features

- Enter customer support tickets through a user-friendly interface
- Automatically classify tickets into support categories
- Predict ticket priority levels (Low, Medium, High, Critical)
- Display confidence scores for predictions
- Color-coded priority indicators for easier interpretation
- Quick example tickets for testing and demonstrations
- Wide dashboard layout with ticket input and prediction results displayed side-by-side

### Dashboard Workflow

1. Enter a customer support ticket
2. Click the **Predict** button
3. View the predicted:
   - Ticket Category
   - Priority Level
   - Model Confidence Scores
4. Use the results to assist with ticket routing and prioritization

### Example Output

**Input Ticket**

> I was charged twice for my subscription and need a refund.

**Predicted Category**

> Billing Inquiry

**Predicted Priority**

> High


## Business Value

This solution can help organizations:

### Faster Ticket Routing

Automatically direct tickets to the correct support team.

### Improved Response Times

Identify urgent tickets earlier.

### Reduced Manual Work

Minimize time spent sorting incoming requests.

### Better Customer Experience

Ensure important issues receive attention quickly.



## Project Structure

```text
Support-Ticket-Classification/
│
├── data/
│   └── customer_support_tickets.csv
│
├── notebooks/
│   └── support_ticket_classifier.ipynb
│
├── models/
│   ├── ticket_type_model.pkl
│   ├── priority_model.pkl
│   └── vectorizer.pkl
│
├── app/
│   └── app.py
│
├── README.md
├── requirements.txt
```

##  How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app/app.py
```


## Key Skills Demonstrated

- Natural Language Processing (NLP)
- Text Classification
- Machine Learning
- Feature Engineering
- Model Evaluation
- Streamlit Deployment
- Data Preprocessing
- Python Development

---

## Author

**Charles Mawewe**

Data Science Student | Aspiring Data Engineer | Machine Learning