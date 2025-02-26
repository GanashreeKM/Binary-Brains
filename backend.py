# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:50:06 2025

@author: 91998
"""
import os
print(os.path.exists(r"C:\Users\91998\Desktop\AIinnovation\student_Learning_data_100.csv"))
from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("C:\\Users\\91998\\Desktop\\AIinovation\\student_learning_data_100.csv")
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(df.to_dict(orient="records"))

@app.route("/learning_gaps", methods=["GET"])
def get_learning_gaps():
    gaps = df[["Name", "Learning_Gap"]].to_dict(orient="records")
    return jsonify(gaps)

@app.route("/student/<int:student_id>", methods=["GET"])
def get_student(student_id):
    student = df[df["Student_ID"] == student_id].to_dict(orient="records")
    return jsonify(student if student else {"error": "Student not found"})

if __name__ == "__main__":
   app.run(debug=True)

