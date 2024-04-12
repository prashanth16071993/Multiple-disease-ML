# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 09:13:41 2023

@author: HP
"""
import numpy as np
from pathlib import Path
import pickle
import streamlit as st
import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['abc','def']).generate()
import yaml
from yaml.loader import SafeLoader
with open("C:/PROJECTMLL/user.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
name, authentication_status, username = authenticator.login('Login', 'main')

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')
    
    