import flask
from flask import Flask,render_template,request
import os
import sys
import numpy as np
from sklearn.linear_model import LinearRegression

from main import reg

app = Flask(__name__)
@app.route('/')
def initial_fun():
    return render_template("index.html")

@app.route("/predict",methods = ['GET','POST'])
def fun():
    try:
        a = []
        for value in request.form.values():
            if value == "Yes":
                a.append(1)
            elif value == "No":
                a.append(0)
            else:
                a.append(float(value))
        b = [np.array(a)]
        sol = reg.reg.predict(b)[0]
        return render_template("index.html" , test_pred = sol)
    except Exception as e:
        err_ty, err_msg, err_line = sys.exc_info()
        print(f"Error from line no : {err_line.tb_lineno},due to {err_ty} reason was : {err_msg}")

if __name__ == "__main__":
        app.run(debug=True)
