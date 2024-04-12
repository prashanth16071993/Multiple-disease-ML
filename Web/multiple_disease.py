# -*- coding: utf-8 -*-


import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth



#hashed_passwords = stauth.Hasher(['abc','def']).generate()


# loading the saved models
diabetes_model = pickle.load(open('C:\PROJECTML/saved_models/trained_model.sav', 'rb'))

heart_disease_model = pickle.load(open('C:\PROJECTML/saved_models/heart_model.sav','rb'))

liver_model = pickle.load(open('C:\PROJECTML/saved_models/liver_model.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Mellitus Prediction',
                           'Heart Disease Prediction',
                           'Liver Disease Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
import yaml
from yaml.loader import SafeLoader
with open("C:\PROJECTML/user.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate( 
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('Login', 'main')


    
if st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')
elif st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
       
    # Diabetes Prediction Page
    if (selected == 'Diabetes Mellitus Prediction'):
        
        # page title
        st.title('Diabetes Prediction using ML')
    
        
        # getting the input data from the user
        col1, col2, col3 = st.columns(3)
        
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')
            
        with col2:
            Glucose = st.text_input('Glucose Level')
        
        with col3:
            BloodPressure = st.text_input('Blood Pressure value')
        
        with col1:
            SkinThickness = st.text_input('Skin Thickness value')
        
        with col2:
            Insulin = st.text_input('Insulin Level')
        
        with col3:
            BMI = st.text_input('BMI value')
        
        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
        
        with col2:
            Age = st.text_input('Age of the Person')
        
        
        # code for Prediction
        diab_diagnosis = ''
        
        # creating a button for Prediction
        
        if st.button('Diabetes Test Result'):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
            
            if (diab_prediction[0] == 1):
              diab_diagnosis = 'The person is diabetic'
            else:
              diab_diagnosis = 'The person is not diabetic'
            
        st.success(diab_diagnosis)
    
    
    
    # Heart Disease Prediction Page
    if (selected == 'Heart Disease Prediction'):
        
        # page title
        st.title('Heart Disease Prediction using ML')
        
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            age = st.text_input('Age')
            
        with col2:
            sex = st.text_input('Sex')
            
        with col3:
            cp = st.text_input('Chest Pain types')
            
        with col1:
            trestbps = st.text_input('Resting Blood Pressure')
            
        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')
            
        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
            
        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')
            
        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')
            
        with col3:
            exang = st.text_input('Exercise Induced Angina')
            
        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')
            
        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')
            
        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')
            
        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
            
            
         
         
        # code for Prediction
        heart_diagnosis = ''
        
        # creating a button for Prediction
        
        if st.button('Heart Disease Test Result'):
            heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
            
            if (heart_prediction[0] == 1):
              heart_diagnosis = 'The person is having heart disease'
            else:
              heart_diagnosis = 'The person does not have any heart disease'
            
        st.success(heart_diagnosis)
            
        
        
    
    # Liver Prediction Page
    if (selected == "Liver Disease Prediction"):
        
        # page title
        st.title("Liver Disease Prediction using ML")
        
    
        
        col1, col2, col3, col4, col5 = st.columns(5)  
        
        with col1:
            Age = st.text_input('Age')
            
        with col2:
            Gender = st.text_input('Gender')
            
        with col3:
            Total_Bilirubin = st.text_input('Total_Bilirubin')
            
        with col4:
            Direct_Bilirubin = st.text_input('Direct_Bilirubin')
            
        with col5:
            Alkaline_Phosphotase = st.text_input('Alkaline_Phosphotase')
            
        with col1:
            Alamine_Aminotransferase = st.text_input('Alamine_Aminotransferase')
            
        with col2:
            Aspartate_Aminotransferase = st.text_input('Aspartate_Aminotransferase')
            
        with col3:
            Total_Protiens = st.text_input('Total_Protiens')
            
        with col4:
            Albumin = st.text_input('Albumin')
            
        with col5:
            Albumin_and_Globulin_Ratio = st.text_input('Albumin_and_Globulin_Ratio')
            
    
            
        
        
        # code for Prediction
        liver_diagnosis = ''
        
        # creating a button for Prediction    
        if st.button("Liver Test Result"):
            liver_prediction = liver_model.predict([[Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])                          
            
            if (liver_prediction[0] == 1):
              liver_diagnosis = "The person has Liver disease"
            else:
              liver_diagnosis = "The person does not have Liver disease"
            
        st.success(liver_diagnosis)
    
        