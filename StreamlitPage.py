# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:01:26 2022

@author: Philanoe
-- FRONT --
Streamlit Functions for the Multi-context question answering chatbot
"""

import streamlit as st
from requests import get


def DisplayText(Text):
    st.write(Text)

def load_lottieurl(url):
    r = get(url)
    if r.status_code != 200:
        return None
    return r.json()

def InitStreamLitPage():
    st.set_page_config(page_title="ChatBot", page_icon="🍂",layout="wide")
    
def Introduction():
    st.subheader("Hi, I am a Chatbot :robot_face: :speech_balloon: :wave:")

    st.write("I am passionate about anwering your questions.")

def UserInput():
    st.text(" ")
    return st.text_input("Please enter your question : ")

def AnswerUser(Text):
    FullString = f'The answer is : "{Text}"'
    st.write(FullString)


