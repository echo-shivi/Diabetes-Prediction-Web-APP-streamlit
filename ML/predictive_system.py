# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pickle

# Load the trained model
loaded_model = pickle.load(open(r'C:\Users\SHIVI\Downloads\Ml\trained_model.sav', 'rb'))

# Define input data
input_data = (5, 166, 72, 19, 175, 25.8, 0.587, 51)

# Convert input data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Make prediction
prediction = loaded_model.predict(input_data_reshaped)

# Print prediction
if prediction[0] == 0:
    print('The person is not diabetic')
else:
    print('The person is diabetic')

