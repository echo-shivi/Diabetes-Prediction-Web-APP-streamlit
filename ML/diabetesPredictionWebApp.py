# -*- coding: utf-8 -*-
"""
Created on Mon May  6 12:20:36 2024

@author: SHIVI
"""
import numpy as np
import pickle
import streamlit as st
from PIL import Image

import requests

# Function to download the trained model file from GitHub
def download_model():
    url = "https://github.com/echo-shivi/diabetesprediction/raw/main/trained_model.sav"
    response = requests.get(url)
    with open("trained_model.sav", "wb") as f:
        f.write(response.content)

# Load the trained model
def load_model():
    download_model()  # Download the model file if not already downloaded
    loaded_model = pickle.load(open("trained_model.sav", "rb"))
    return loaded_model

# Load the trained model
loaded_model = load_model()

# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
def main():
    
    
 

    # Setting title 
    st.title('Diabetes Prediction Web App')
   
    
    # getting the input data from the user
    
    
    # Getting input data from the user
    with st.container():
  
   
        st.write("Please enter the following details:")
        
        pregnancies = st.number_input('Number of Pregnancies', value=0)
        glucose = st.number_input('Glucose Level', value=0)
        blood_pressure = st.number_input('Blood Pressure value', value=0)
        skin_thickness = st.number_input('Skin Thickness value', value=0)
        insulin = st.number_input('Insulin Level', value=0)
        bmi = st.number_input('BMI value', value=0.0)
        diabetes_pedigree_function = st.number_input('Diabetes Pedigree Function value', value=0.0)
        age = st.number_input('Age of the Person', value=0)
        
        # Button for Prediction
        if st.button('Diabetes Test Result'):
            diagnosis = diabetes_prediction([pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age])
            st.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()
    
    
