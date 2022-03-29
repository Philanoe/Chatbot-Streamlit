# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:47:14 2022

@author: Philanoe
-- FRONT --
Module aiming at communicating with the FastAPI app
"""

import requests
API_url = 'http://127.0.0.1:8080/'

def QuestionAnswering(Question):
    
    Option_url = 'question/'
    Data_url = Question
    Full_url = API_url + Option_url + Data_url
    
    try:
        BackToFrond_Data = requests.get(Full_url)
        Answer = BackToFrond_Data.json()["answer"]
        pass
    except Exception:
        Answer = 'API connexion error'
        
    return Answer