# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:01:26 2022

@author: Philanoe
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

Revision = 'v1.0'
app.InitStreamLitPage()
app.DisplayText(f'code revision : {Revision}')
Question = app.UserInput("Please enter your question : ")
Answer = FrontToBack.QuestionAnswering(Question)
app.DisplayText(f'Answer : {Answer}')


