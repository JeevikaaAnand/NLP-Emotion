# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 16:24:51 2023

@author: Jeevika
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st

pickle_in = open("E:/Userfiles/Desktop/Python/project/NLP.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def Emotion_prediction(Lemma_text):
    
    prediction=classifier.predict([[Lemma_text]])
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

    Lemma_text = st.text_input('Enter a comment')
    
    Emotion = ''
    
    if st.button('Emotion Result'):
        Emotion = Emotion_prediction(Lemma_text)
        
    st.success(Emotion)
    
    
    
    
if __name__ == '__main__':
    main()

 




