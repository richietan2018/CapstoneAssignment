__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

import streamlit as st
import pandas as pd
from io import StringIO
from logics.requirements_recommendations_handler import get_requirements_recommendations 
from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Requirement's & Recommendation's"
)
# endregion <--------- Streamlit App Configuration --------->

#HEADER
st.title("Requirement's & Recommendation's")

userInput = ""

#Upload details or enter details 
detailsType = st.radio(
    "Will you like to enter your dream house details or Upload your dream house details?",
    ["Enter mine/our dream house details","Upload mine/our dream house details"],
    index=None,
)
st.write("You selected:", detailsType)
st.divider()

if (detailsType == "Enter mine/our dream house details"):
    form = st.form(key="form")
    user_prompt = form.text_area("**Step 1: Enter dream house details!**", height=50
            , placeholder="I will love to stay in Punggol, best to be near MRT Station and nearby should have primary schools.")
    userInput = user_prompt

    url = form.text_area("**Step 2: Enter the house link to check if is dream home**", height=20
            , placeholder="https://www.propnex.com/listing-details/578521/272a-punggol-walk")
    
    if form.form_submit_button("Submit"):
        if userInput == "" or url == "":
            st.error("All fields are mandatory.")
        else:
            st.toast(f"Your input - {url} as been submitted. Please give us a moment.")
            st.divider()
            rawResults,homeResearchAgentReplies, buyerDreamAgentReplies, housing_agentReplies = get_requirements_recommendations(userInput,url)
            st.write(rawResults)


elif (detailsType == "Upload mine/our dream house details"):
    uploaded_file = st.file_uploader("**Step 1: Upload the details of your dream house!**")
    if uploaded_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        input = stringio.read()

        userInput = input

    form = st.form(key="form")
    url = form.text_area("**Step 2: Enter the house link to check if is dream home**", height=20
            , placeholder="https://www.propnex.com/listing-details/575251/413a-fernvale-link")
    
    if form.form_submit_button("Submit"):
        if userInput == "" or url == "":
            st.error("All fields are mandatory.")
        else:
            st.toast(f"Your input - {url} as been submitted. Please give us a moment.")
            st.divider()
            rawResults,homeResearchAgentReplies, buyerDreamAgentReplies, housing_agentReplies = get_requirements_recommendations(userInput,url)
            st.write(rawResults)


#FOOTER
st.divider()
with st.expander("IMPORTANT NOTICE"):
    st.write("1. This web application is a prototype developed for educational purposes only.")
    st.write("2. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.")
    st.write("3. Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.")
    st.write("4. Always consult with qualified professionals for accurate and personalized advice.")
