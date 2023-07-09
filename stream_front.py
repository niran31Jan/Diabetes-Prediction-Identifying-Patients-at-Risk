import streamlit as st
import pickle
import numpy as np
st.title('Do you have diabetes :relieved: or not :smile: ?')
st.title('Check Here :point_down:')
gender=st.selectbox('Gender',('Female','Male','Other'))
age=st.text_input('Enter your age')
hypertension=st.selectbox('Hypertension',('Yes','No'))
heart_disease=st.selectbox('Heart Disease',('Yes','No'))
if hypertension=='Yes':
    hypertension=1
elif hypertension=='No':
    hypertension=0
else:
    print('wrong input')


if heart_disease=='Yes':
    heart_disease=1
elif heart_disease=='No':
    heart_disease=0
else:
    print('wrong input')

smoking_history=st.selectbox('Select Your Smoking History',('No Info','Never','Former','Current','Not Current','Ever'))
bmi=st.text_input('Enter your body mass index')
HbA1c_level=st.text_input('Enter your Hemoglobin A1c')
blood_glucose_level=st.text_input('Enter your blood glucose level')

def submit_button():
    pipe=pickle.load(open('diabetes_pipe.pkl','rb'))
    test_input=np.array([gender,age,hypertension,heart_disease,smoking_history,bmi,HbA1c_level,blood_glucose_level],dtype=object).reshape(1,8)
    result=pipe.predict(test_input)

    if result==0:
        st.success('No Diabetes :thumbsup:')
    else:
        st.error('Yes Diabetes :thumbsdown:')

submit=st.button('Submit',on_click=submit_button)

