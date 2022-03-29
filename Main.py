#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:45:01 2022

@author: jingpan
-- FRONT --
Main module of the front end of a 
multi-context question answering chatbot

Ask a question Q
    Question = UserInput()
Find the label
    Label = Classifier(Question)
Get the context data related to this label
    Context = GetContext(Label)
Get the answer from the context data
    Answer = QuestionAnswering(Question, Context)
Answer the user
    AnswerUser(Answer)
    
Finally, the label classification and context based question answering
will be dealt with in the back end
So, here, we have just a QuestionAnswering function
"""

import StreamlitPage as app
import FrontToBack
import streamlit as st
from streamlit_lottie import st_lottie

app.InitStreamLitPage()

extra_column, text_column, image_column = st.columns((1,3,2.5))

lottie_hello = app.load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_jh9gfdye.json")

with text_column:
    app.Introduction()
    Question = app.UserInput()
    Answer = FrontToBack.QuestionAnswering(Question)
    app.AnswerUser(Answer)

with image_column:
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="low", # medium ; high
        # canvas
        height=600,
        width=400,
        key=None,
    )