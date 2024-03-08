# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 03:37:18 2024

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import base64


st.set_page_config(
        page_title="Multiple Disease Risk Predictor" 
)

def sidebar_bg(side_bg):

   side_bg_ext = 'png'

   st.markdown(
      f"""
      <style>
      [data-testid="stSidebar"] > div:first-child {{
          background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()});
          background-size: cover;
      }}
      </style>
      """,
      unsafe_allow_html=True,
      )
def set_background(main_bg):
    '''
    A function to unpack an image from root folder and set as bg.
 
    Returns
    -------
    The background.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_background('healthc.avif') 
sidebar_bg('images.jpg')

# Loading the saved models

diabetes_model = pickle.load(open('rf_diabetes_.pkl', 'rb'))


thyroid_model = pickle.load(open('rf_thyroid.pkl', 'rb'))


heart_model = pickle.load(open('svc_heart.pkl', 'rb'))
# sidebar for navigation



with st.sidebar:
    selected = option_menu('Multiple Disease Risk Prediction System',
                           ['Diabetes Risk Prediction',
                            'Thyroid Disease Risk Prediction', 'Heart Disease Risk Prediction'],
                           icons = ['activity', 'person', 'heart-pulse-fill'],
                           default_index = 0)

# Diabetes Prediction page
if (selected == 'Diabetes Risk Prediction'):
    
      
    
    
    # page title
    st.title('Diabetes Mellitus Risk Prediction')
    
    
    gender = st.selectbox('Gender', ['Male', 'Female', 'Choose not to disclose'])
    
    
    age = st.number_input('Age : ', step = 1, value = None, placeholder = "Input your age")
    
    
    height = st.number_input('Height (cm) : ', step = 1, value = None, placeholder = "Input your Height")
    
    
    weight = st.number_input('Weight (kg) : ', step = 1, value = None, placeholder = "Input your Weight")
    
    
    HbA1c_level = st.number_input('HbA1c Level : ', step = 0.1,value = None, placeholder = "Input your current Glycated Haemoglobin level or HbA1c level")
    
    
    blood_glucose_level = st.number_input('Blood Glucose Level : ', step = 1, value = None, placeholder = "Input your Blood Glucose Level")
    
    if age:
        
        if age > 18 and age <= 40:
        
            age_group_young = 1
        
        else:
        
            age_group_young = 0
        
        if age > 60:
        
            age_group_senior = 1
        
        else:
        
            age_group_senior = 0
        
        
    if blood_glucose_level:
        
        if blood_glucose_level > 70 and blood_glucose_level <= 140:
        
            glucose_category_normal = 1
        
        else:
        
            glucose_category_normal = 0
        
        if blood_glucose_level > 200:
        
            glucose_category_risky = 1
            
        else:
            
            glucose_category_risky = 0
            
            
    if height:
        
        if weight:
            
             bmi = weight * ((height/100)**2)
    
             if bmi > 30.0:
                 
                 bmi_category_obese = 1
                 
             else:
                 
                 bmi_category_obese = 0         
        
        
    smoke = st.selectbox('Do you smoke ? : ', ['Currently', 'Not Currently', 'Never'])
    
    
    if smoke.lower() == 'never':
        
        smoking_history_never = 1
        
    else:
        
        smoking_history_never = 0
        
        
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result : '):
        try:
        
                diab_prediction = diabetes_model.predict_proba(pd.DataFrame([age, bmi, HbA1c_level, blood_glucose_level, age_group_young, age_group_senior,
                                                           glucose_category_normal, glucose_category_risky,
                                                           bmi_category_obese, smoking_history_never]).T)
        except NameError:

                st.error('Input Values For Height and Weight')
        
        
        if diab_prediction[0][1] >= 0.5:
        
            st.write('**Diabetes Risk : :red[{}%]**'.format(round(diab_prediction[0][1] * 100)))
            
        else:
            
            st.write('**Diabetes Risk : :green[{}%]**'.format(round(diab_prediction[0][1] * 100)))
            
    
    
 ###################################################################################################################################################################       
    
    
if (selected == 'Thyroid Disease Risk Prediction'):
    
    
    
    # page title
    st.title('Thyroid Risk Prediction')
    
    
    sex = st.selectbox('Sex', ['Male', 'Female', 'Choose not to disclose'])
    
    
    if sex == 'Male':
        
        sex_M = 1
        
    else:
        
        sex_M = 0
        
    
    age_thy = st.text_input('Age : ', value = None, placeholder = "Input your age")
    
    
    surgery = st.selectbox('Thyroid Surgery? ', ['Yes', 'No'], help = 'Have you had a thyroid surgery before?')
                              
    if surgery.lower =='yes':
        
        thyroid_surgery = 1
        
    else:
        
        thyroid_surgery = 0
    
    
    tumor_str = st.selectbox('Thyroid Tumors? ', ['Yes', 'No'], help = 'Do you have a thyroid tumor?')
                              
    if tumor_str.lower =='yes':
        
        tumor = 1
    else:
        
        tumor = 0
        
        
    psy = st.selectbox('Psychiatric History? ', ['Yes', 'No'], help = 'Do you have a psychiatric history?')
                              
    if psy.lower =='yes':
        
        psych = 1
        
    else:
        
        psych = 0
        
        
    TSH= st.number_input('TSH Level : ', step = 0.1, value = None, placeholder = "Input your TSH levels")
    
    
    T3 = st.number_input('T3 level : ', step = 0.1, value = None, placeholder = "Input your T3 level")
    
    
    TT4 = st.number_input('TT4 level : ', step = 0.1, value = None, placeholder = "Input your TT4 level")
    
    
    T4U = st.number_input('T4U Level : ', step = 0.1,value = None, placeholder = "Input your T4U level")
    
    
    FTI = st.number_input('FTI Level : ', step = 0.1,value = None, placeholder = "Input your FTI level")
    
    
    thy_diagnosis = ''
    
    if st.button('Thyroid Disease Test Result : '):
        
        thy_prediction = thyroid_model.predict_proba(pd.DataFrame([age_thy, thyroid_surgery, tumor, psych,
                                                             TSH, T3, TT4, T4U, FTI, sex_M]).T)
        
        if thy_prediction[0][1] == thy_prediction.max():
        
            st.write('**Hypothyroidism Risk : :red[{} %]**'.format(round(thy_prediction[0][1] * 100)))
            
            st.write('**Hyperthyroidism Risk : :green[{} %]**'.format(round(thy_prediction[0][2] * 100)))
            
            
        elif thy_prediction[0][2] == thy_prediction.max():
        
            st.write('**Hypothyroidism Risk : :green[{} %]**'.format(round(thy_prediction[0][1] * 100)))
            
            st.write('**Hyperthyroidism Risk : :red[{} %]**'.format(round(thy_prediction[0][2] * 100)))
            
        else:
            
        
            st.write('**Hypothyroidism Risk : :green[{} %]**'.format(round(thy_prediction[0][1] * 100)))
            
            st.write('**Hyperthyroidism Risk : :green[{} %]**'.format(round(thy_prediction[0][2] * 100)))
            
        
        
 #######################################################################################################################################################################   


if (selected == 'Heart Disease Risk Prediction'):

        # page title
     st.title('Heart Disease Risk Prediction')
    
    
     age_h = st.text_input('Age : ', value = None, placeholder = "Input your age")
     
     
     gender_h = st.selectbox('Gender', ['Male', 'Female']) 
     
     
     if gender_h == 'Male':
         
         
         sex_m = 1
         
     else:
         
         sex_m = 0
         
        
     resting_bp = st.text_input('Resting Blood Pressure : ', value = None, placeholder = "Input your Resting Blood Pressure")
     
     
     chol = st.number_input('Cholesterol Level : ',step = 1, value = 0, placeholder = "Input your Cholesterol Level")
     
     
     fast = st.number_input('Fasting Blood Sugar(mg/dl) : ', step = 1, value = 0, placeholder = "Input your Fasting Blood Sugar")
     
     
     if fast >= 120:
         
         fasting_bs = 1
         
     else:
         
         fasting_bs = 0
         
     max_hr = st.text_input('Maximum Heart Rate : ', value = None, placeholder = "Input your Maximum Heart Rate")
     
     
     oldpeak = st.number_input('Oldpeak Value : ', step = 0.1,value = None, placeholder = "Input your Oldpeak value")
     
     
     chest_pain = st.selectbox('Chest Pain type', ['Atypical Angina', 'Typical Angina', 'Non-Angina Pain', 'Asymptomatic Chest Pain'])
     
     
     if chest_pain == 'Atypical Angina':
         
         chest_ata = 1
         
     else:
         
         chest_ata = 0
         
         
     if chest_pain == 'Typical Angina':
         
         chest_ta = 1
         
     else:
         
         chest_ta = 0
         
     if chest_pain == 'Non-Angina Pain':
         
         chest_nap = 1
         
     else:
         
         chest_nap = 0
         
         
     rest_ecg = st.selectbox('Resting ECG', ['Normal', 'ST', 'LVH'], help = 'Resting ECG result')
     
     
     if rest_ecg == 'Normal':
         
         rest_ecg_normal = 1
         
     else:
         
         rest_ecg_normal = 0
         
     exercise_ang = st.selectbox('Do you experience exercise-induced angina or chest pain', ['Yes', 'No'])
     
     
     if exercise_ang == 'Yes':
         
         exer_ang_y = 1
         
     else:
         
         exer_ang_y = 0
         
     st_slope = st.selectbox('ST Slope', ['Down', 'Flat', 'Up'], help = 'This refers to the slope of the peak exercise ST segment')
     
     
     if st_slope == 'Flat':
         
         st_slope_flat = 1
         
     else:
         
         st_slope_flat = 0
         
         
     if st_slope == 'Up':
         
        st_slope_up = 1
        
     else:
         
        st_slope_up = 0 
        
        
     if chol > 240:
         
         chol_high = 1
         
     else:
         
         chol_high = 0
         
         
     heart_diagnosis = ''
     
     
     if st.button('Heart Disease Test Result : '):
         
         
         heart_prediction = heart_model.predict_proba(pd.DataFrame([age_h, resting_bp, chol, fasting_bs,
                                                max_hr, oldpeak, sex_m, chest_ata, chest_nap,
                                                chest_ta, rest_ecg_normal, exer_ang_y, st_slope_flat,
                                                st_slope_up, chol_high]).T)
         
         
         if heart_prediction[0][1] >= 0.5:
         
             st.write('**Heart Disease Risk : :red[{}%]**'.format(round(heart_prediction[0][1] * 100)))
             
         else:
             
             st.write('**Heart Disease Risk : :green[{}%]**'.format(round(heart_prediction[0][1] * 100)))
         
