# 🎓 Student Performance Prediction Using Machine Learning and Flask

##  Project Description

Student Performance Prediction is an end-to-end Machine Learning web application developed using Python, Object-Oriented Programming (OOP), Flask Framework, HTML, and Pickle Serialization. The purpose of this project is to predict a student's Performance Index based on various academic and lifestyle factors.

This project demonstrates the complete Machine Learning workflow, starting from data collection and preprocessing to model training, evaluation, deployment, and prediction through a web interface.

Users can enter student information through the frontend webpage, and the application predicts the student's expected Performance Index using a trained Linear Regression model.

---

#  Problem Statement

Educational institutions often need to analyze student performance based on study habits and other influencing factors.

The objective of this project is to build a Machine Learning model that predicts the Performance Index of a student using the following features:

- Hours Studied
- Previous Scores
- Extracurricular Activities
- Sleep Hours
- Sample Question Papers Practiced

The predicted output is:

- Performance Index

---

#  Dataset Information

The dataset used in this project contains student academic and lifestyle information.

### Input Features (X)

| Feature Name | Description |
|-------------|-------------|
| Hours Studied | Number of hours studied by the student |
| Previous Scores | Previous academic scores |
| Extracurricular Activities | Participation in extracurricular activities |
| Sleep Hours | Average sleep hours |
| Sample Question Papers Practiced | Number of sample papers practiced |

### Target Variable (Y)

| Target |
|----------|
| Performance Index |

---

# 🔄 Data Preprocessing

Before training the model, data preprocessing was performed.

### Categorical Encoding

The feature:

```python
Extracurricular Activities
```

was converted into numerical values:

```python
Yes = 1
No = 0
```

This transformation allows the Machine Learning algorithm to process categorical data effectively.

---

#  Object-Oriented Programming (OOP)

The project follows Object-Oriented Programming concepts through the implementation of an `MLR` class.

### Class Responsibilities

The class is responsible for:

- Reading the dataset
- Data preprocessing
- Feature selection
- Train-test splitting
- Model training
- Model testing
- Prediction generation
- Model serialization

---

#  Methods Implemented

## 1. __init__()

This method:

- Loads the dataset
- Displays dataset information
- Checks for null values
- Performs preprocessing
- Splits data into training and testing sets
- Initializes Linear Regression

---

## 2. training()

This method:

- Trains the Linear Regression model
- Calculates training metrics
- Saves the trained model as a Pickle file

Metrics calculated:

- R² Score
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## 3. testing()

This method evaluates the model using test data.

Metrics calculated:

- R² Score
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## 4. sample_input()

This method accepts user inputs and predicts the Performance Index using the trained model.

---

#  Machine Learning Model

### Algorithm Used

```python
LinearRegression()
```

### Why Linear Regression?

Linear Regression is suitable for predicting continuous numerical values and works efficiently when there is a linear relationship between input features and the target variable.

---

#  Train-Test Split

The dataset is divided into:

```python
train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

### Distribution

- Training Data = 80%
- Testing Data = 20%

This ensures proper evaluation of model performance.

---

#  Model Evaluation

The model performance is evaluated using:

## R² Score

Measures how well the model explains the variance in the data.

## Mean Squared Error (MSE)

Measures the average squared difference between actual and predicted values.

## Root Mean Squared Error (RMSE)

Measures the average prediction error in the same unit as the target variable.

---

#  Model Serialization Using Pickle

After successful training, the model is converted into a Pickle file.

```python
with open("student_performance.pkl", "wb") as f:
    pickle.dump(self.reg, f)
```

Benefits:

- No need to retrain the model every time
- Faster prediction
- Easy deployment

Generated File:

```text
student_performance.pkl
```

---

#  Flask Web Application

Flask is used to connect the Machine Learning model with the frontend.

The web application consists of two routes.

## Home Route

```python
@app.route('/')
```

Purpose:

- Loads the homepage
- Displays the input form

---

## Prediction Route

```python
@app.route('/predict', methods=['GET', 'POST'])
```

Purpose:

- Receives user input
- Converts categorical values
- Sends data to the trained model
- Generates prediction
- Displays result on the webpage

---

#  Prediction Workflow

### Step 1

User enters:

- Hours Studied
- Previous Scores
- Extracurricular Activities
- Sleep Hours
- Sample Papers Practiced

### Step 2

Data is converted into numerical format.

```python
Yes → 1
No → 0
```

### Step 3

Input data is passed to the trained Linear Regression model.

```python
prediction = reg.reg.predict(input_data)
```

### Step 4

The model predicts the student's Performance Index.

### Step 5

The predicted result is displayed on the webpage.

---

# 🎨 Frontend Development

A frontend webpage was created using HTML.

The webpage contains:

- Input fields for all features
- Submit button
- Prediction result display section

The frontend collects user data and sends it to Flask for prediction.

---

#  Project Structure

```text
Student-Performance-Prediction/
│
├── app.py
├── main.py
├── student_performance.pkl
├── Student_Performance.csv
├── requirements.txt
├── Procfile
│
├── templates/
│   └── index.html
│
└── README.md
```

---

#  Requirements File

A requirements file is included to install all necessary libraries.

### requirements.txt

```text
numpy
pandas
scikit-learn
matplotlib
seaborn
flask
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

#  Deployment Preparation

To make deployment easier, a Procfile is included.

The Procfile helps connect:

- Frontend
- Flask Backend
- Machine Learning Model

This allows the application to be deployed on cloud platforms such as:

- Render
- Heroku
- Railway

After deployment, a public URL can be generated for users to access the application online.

---

#  Sample Prediction

### Input

```text
Hours Studied = 7
Previous Scores = 80
Extracurricular Activities = Yes
Sleep Hours = 8
Sample Papers Practiced = 6
```

### Output

```text
Predicted Performance Index = Generated by the Trained Model
```

---

#  Features of the Project

✅ Machine Learning Model

✅ Linear Regression Algorithm

✅ Object-Oriented Programming (OOP)

✅ Data Preprocessing

✅ Model Training

✅ Model Testing

✅ Performance Evaluation

✅ Pickle Serialization

✅ Flask Backend

✅ HTML Frontend

✅ Real-Time Prediction

✅ Requirements File

✅ Procfile Configuration

✅ Deployment Ready

---

#  Project Outcome

Successfully developed a complete Machine Learning web application capable of predicting student performance based on academic and lifestyle factors.

The project demonstrates practical implementation of:

- Python Programming
- Object-Oriented Programming
- Data Analysis
- Machine Learning
- Flask Development
- Model Deployment
- Frontend and Backend Integration

---

#  Author

## Bavana

**Role:** Data Analyst Intern

### Project Title

**Student Performance Prediction Using Machine Learning and Flask Framework**

This project showcases an end-to-end Machine Learning pipeline, from data preprocessing and model training to deployment using Flask, providing real-time student performance prediction through an interactive web interface.
