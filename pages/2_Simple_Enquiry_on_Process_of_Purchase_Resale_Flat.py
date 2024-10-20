import streamlit as st
import pandas as pd
import numpy as np
from logics.resale_flat_process_handler import process_resale_flat_process_message
from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Simple enquiry on process of purchasing resale flat"
)
# endregion <--------- Streamlit App Configuration --------->

#Page Title
st.title("Simple enquiry on process of purchasing resale flat")

#Planning 
agentBool = st.radio(
    "Are you planning to engage for an Agent for your resale flat purchase?",
    ["Yes, I/We decided to engage an agent!","No, I/We decided not to engage an agent!"],
    index=None,
)
st.write("You selected:", agentBool)

response = process_resale_flat_process_message(agentBool)
st.divider()
st.write(response)

#FOOTER
st.divider()
with st.expander("IMPORTANT NOTICE"):
    st.write("1. This web application is a prototype developed for educational purposes only.")
    st.write("2. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.")
    st.write("3. Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.")
    st.write("4. Always consult with qualified professionals for accurate and personalized advice.")
