import numpy as np
import pickle
import streamlit as st


pipe=pickle.load(open('diabetes_pipe.pkl','rb'))
test_input=np.array(['Female',44,1,0,'never',19.31,6.5,250],dtype=object).reshape(1,8)
result=pipe.predict(test_input)

if result==0:
    print('No Diabetes')
else:
    print('Yes Diabetes')