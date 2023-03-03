# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:24:51 2023

@author: Jeevika
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st

pickle_in = open("NLP1.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def Emotion_prediction(Comments):
    
    prediction=classifier.predict([[sub]])
    print(prediction)
    
    if (prediction[0] == 0):
        return 'Emotion - Neutral'
    else:
        return 'Emotion -Positive'

def main():
    st.title('emotion Prediction Web App')
    st.header('User Input Parameters')
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Emotion Prediction App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)

    Comments = st.text_input('Enter a comment')
    
    Emotion = ''
    
    if st.button('Emotion Result'):
        Emotion = Emotion_prediction(sub)
        
    st.success(Emotion)
    
    
    
    
if __name__ == '__main__':
    main()

 




