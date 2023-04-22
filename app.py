import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('heart_disease_model.pkl', 'rb'))


# Define the function to predict heart disease
def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)
    return prediction


# Define the Streamlit app
def app():
    st.title('Heart Disease Prediction')
    st.write('Please input the following parameters to predict the presence of heart disease:')

    # Create sliders and dropdowns for user input
    age = st.slider('Age', 20, 100, 50)
    sex = st.selectbox('Sex', [0, 1])
    cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
    trestbps = st.slider('Resting Blood Pressure (mm Hg)', 80, 200, 120)
    chol = st.slider('Cholesterol (mg/dL)', 100, 600, 200)
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', [0, 1])
    restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])
    thalach = st.slider('Maximum Heart Rate Achieved', 70, 220, 150)
    exang = st.selectbox('Exercise Induced Angina', [0, 1])
    oldpeak = st.slider('ST Depression Induced by Exercise Relative to Rest', 0.0, 6.0, 3.0, 0.1)
    slope = st.selectbox('Slope of the Peak Exercise ST Segment', [0, 1, 2])
    ca = st.selectbox('Number of Major Vessels Colored by Flourosopy', [0, 1, 2, 3])
    thal = st.selectbox('Thalassemia', [0, 1, 2, 3])

    # When the user clicks the 'Predict' button, make the prediction
    if st.button('Predict'):
        result = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca,
                                       thal)
        if result == 0:
            st.write('No Heart Disease Detected for the Person ')
        else:
            st.write('Heart Disease Detected for the Person!! Consult Doctor Immediately ')


if __name__ == '__main__':
    app()