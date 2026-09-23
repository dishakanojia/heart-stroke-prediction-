import streamlit as st
import pandas as pd
import joblib

model=joblib.load('KNN_heart.pkl')
scaler = joblib.load('scaler.pkl')
expected_columns = joblib.load('columns.pkl')

st.title('Heart Disease Prediction by disha')
st.markdown('This is a simple web app to predict the presence of heart disease based on user input features. Please enter the required information below:')

age = st.slider('age',18,100,40)
sex=st.selectbox('sex', ['Male', 'Female'])
chest_pain_type=st.selectbox('chest pain type', ['typical angina', 'atypical angina', 'non-anginal pain', 'asymptomatic'])
resting_blood_pressure=st.slider('resting blood pressure', 80, 200, 120)
cholesterol=st.number_input('cholesterol (mg/dL)', 100, 600, 200)
fasting_blood_sugar=st.selectbox('fasting blood sugar > 120 mg/dL', ['Yes', 'No'])
rest_ecg=st.selectbox('resting electrocardiographic results', ['normal', 'ST-T wave abnormality', 'left ventricular hypertrophy'])
max_heart_rate=st.slider('maximum heart rate achieved', 60, 220, 150)
exercise_induced_angina=st.selectbox('exercise induced angina', ['Yes', 'No'])
oldpeak=st.number_input('oldpeak (ST depression induced by exercise relative to rest)', 0.0, 10.0, 1.0)
st_slope=st.selectbox('slope of the peak exercise ST segment', ['upsloping', 'flat', 'downsloping'])    

if st.button('Predict'):
    input_data = pd.DataFrame({
        'age': [age],
        'sex': [1 if sex == 'Male' else 0],
        'chest_pain_type': [chest_pain_type],
        'resting_blood_pressure': [resting_blood_pressure],
        'cholesterol': [cholesterol],
        'fasting_blood_sugar': [1 if fasting_blood_sugar == 'Yes' else 0],
        'rest_ecg': [rest_ecg],
        'max_heart_rate': [max_heart_rate],
        'exercise_induced_angina': [1 if exercise_induced_angina == 'Yes' else 0],
        'oldpeak': [oldpeak],
        'st_slope': [st_slope]
    })

    # Ensure the input data has the same columns as expected by the model
    input_data = input_data.reindex(columns=expected_columns, fill_value=0)

    # Scale the input data
    scaled_input_data = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(scaled_input_data)

    # Display result
    if prediction[0] == 1:
        st.error('The model predicts that you may have heart disease. Please consult a healthcare professional for further evaluation.')
    else:
        st.success('The model predicts that you are unlikely to have heart disease. However, please consult a healthcare professional for a comprehensive assessment.')
