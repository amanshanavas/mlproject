# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YWcQ7HaI3UHSRtS1rge7VCXJFirnGVwO
    
    select = st.sidebar.selectbox('Select Form', ['Form 1'], key='2')
    if not st.sidebar.checkbox("Hide Website", True, key='3'):

"""

import pandas as pd
df = pd.read_csv('diabetes.csv')
df.head()

import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix,classification_report
from sklearn.preprocessing import StandardScaler
import pickle

# Split dataset into two sets - Training Set and Test Set
X_train, X_test, y_train, y_test = train_test_split(df[['Pregnancies', 'Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age']], df['Outcome'], test_size=0.2, random_state=109)

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

#Creating the model
logisticRegr = LogisticRegression()
logisticRegr.fit(X_train, y_train)
y_pred = logisticRegr.predict(X_test)

#Saving the Model
pickle_out = open("logisticRegr.pkl", "wb") 
pickle.dump(logisticRegr, pickle_out) 
pickle_out.close()

pickle_in = open('logisticRegr.pkl', 'rb')
classifier = pickle.load(pickle_in)

#Input of Patient Data
st.sidebar.header('Diabetes Prediction App - Made by Aman Shanavas')
st.title('Diabetes Prediction(Only for females above 21 years of    Age)')
name = st.text_input("Name:")
pregnancy = st.number_input("No. of times pregnant:")
glucose = st.number_input("Plasma Glucose Concentration :")
bp =  st.number_input("Diastolic Blood Pressure (mm Hg):")
skin = st.number_input("Triceps Skin Fold thickness (mm):")
insulin = st.number_input("2-Hour serum insulin (mu U/ml):")
bmi = st.number_input("Body Mass Index (weight in kg/(height in m)^2):")
dpf = st.number_input("Diabetes Pedigree Function:")
age = st.number_input("Age:")
    
submit = st.button('Predict')

#Output
if submit:
        prediction = classifier.predict([[pregnancy, glucose, bp, skin, insulin, bmi, dpf, age]])
        st.write(' ')
        if prediction == 0 or prediction == 0.0:
            st.write('Congratulations',name,', you are not Diabetic')
        else:
            st.write(name,", we are sorry to say, but it seems like you are Diabetic.")
           
       

