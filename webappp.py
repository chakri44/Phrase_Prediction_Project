# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 22:04:24 2023

@author: Laksh
"""

import numpy as np
import tensorflow as tf
import streamlit as st
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

with open(r'C:\Users\Laksh\Downloads\book\sherlock-holm.es_stories_plain-text_advs.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    
tokenizer = Tokenizer()
tokenizer.fit_on_texts([text])

model2= tf.keras.models.load_model(r'C:\Users\Laksh\Downloads\model2.h5')

#function
def pred(seed_text,next_words):

    for _ in range(int(next_words)):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=17, padding='pre')
        predicted = np.argmax(model2.predict(token_list), axis=-1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word

    return seed_text


def main():
    
    #title for interface
    st.title("Next Word Prediction Web App")
    
    #getting the input data
    sentence=st.text_input('sentence to complete')
    no_of_words=st.text_input('number_of_words')
    
    str=''
    
    if st.button('Generate Words'):
        str=pred(sentence,no_of_words)
        
    st.success(str)
    
    
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    