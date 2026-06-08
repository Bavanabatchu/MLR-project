import numpy as np
import pandas as pd
import sys
import pickle
import  flask
from flask import Flask,render_template,request
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, root_mean_squared_error
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import os

class MLR:

    def __init__(self, path):
        try:
            self.path = path
            self.df = pd.read_csv(self.path)

            print("First 5 Rows:")
            print(self.df.head(5))

            print("\nDataset Shape:")
            print(self.df.shape)

            print("\nAny Null Values:")
            print(self.df.isnull().values.any())

            print("\nData Types:")
            print(self.df.dtypes)

            self.df["Extracurricular Activities"] = (self.df["Extracurricular Activities"].map({"Yes": 1, "No": 0}))
            self.X = self.df[["Hours Studied","Previous Scores","Extracurricular Activities","Sleep Hours","Sample Question Papers Practiced"]]
            self.y = self.df["Performance Index"]
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X,self.y,test_size=0.2,random_state=42)
            self.reg = LinearRegression()

        except Exception as e:
            err_ty, err_msg, err_line = sys.exc_info()
            print(f"Error from line no : {err_line.tb_lineno},due to {err_ty} reason was : {err_msg}")

    def training(self):
        try:
            self.reg = LinearRegression()
            self.reg.fit(self.X_train, self.y_train)
            train_pred = self.reg.predict(self.X_train)

            print("Training Results")
            print("Training Accuracy (R2):",r2_score(self.y_train, train_pred))
            print("Training MSE:",mean_squared_error(self.y_train, train_pred))
            print("Training RMSE:",root_mean_squared_error(self.y_train, train_pred))
            with open("student_performance.pkl", "wb") as f:
                pickle.dump(self.reg, f)

            print("\nModel Saved Successfully!")


        except Exception as e:
            err_ty, err_msg, err_line = sys.exc_info()
            print(f"Error from line no : {err_line.tb_lineno},due to {err_ty} reason was : {err_msg}")

    def testing(self):
        try:
            test_pred = self.reg.predict(self.X_test)

            print("\nTesting Results")
            print("Testing Accuracy (R2):",r2_score(self.y_test, test_pred))
            print("Testing MSE:",mean_squared_error(self.y_test, test_pred))
            print("Testing RMSE:",root_mean_squared_error(self.y_test, test_pred))


        except Exception as e:
            err_ty, err_msg, err_line = sys.exc_info()
            print(f"Error from line no : {err_line.tb_lineno},due to {err_ty} reason was : {err_msg}")

    def sample_input(self,hours_studied,previous_scores,extracurricular,sleep_hours,sample_papers):
        try:
            result = self.reg.predict([[hours_studied,previous_scores,extracurricular,sleep_hours,sample_papers]])[0]
            print(f"\nSample Prediction : {result:.2f}")
        except Exception as e:
            err_ty, err_msg, err_line = sys.exc_info()
            print(f"Error from line no : {err_line.tb_lineno},due to {err_ty} reason was : {err_msg}")

reg = MLR("Student_Performance.csv")
reg.training()
reg.testing()