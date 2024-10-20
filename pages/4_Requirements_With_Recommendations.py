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

st.write("Step 1: You may choose to upload the details of your dream house OR enter the details into the box below.")

col1, col2 = st.columns(2)

with col1:
    form = st.form(key="form")
    user_prompt = form.text_area("Enter dream house details!", height=50
            , placeholder="I love to stay in Punggol! Best to be near MRT Station")

    if form.form_submit_button("Submit"):
        st.toast(f"Your input - {user_prompt} as been submitted. Please give us a moment.")
        userInput = user_prompt
        #rawResults,homeResearchAgentReplies, buyerDreamAgentReplies, housing_agentReplies = get_requirements_recommendations(user_prompt)
        #st.write(rawResults)

with col2:
    uploaded_file = st.file_uploader("Upload the details of your dream house!")
    if uploaded_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        input = stringio.read()

        userInput = input
        #rawResults,homeResearchAgentReplies, buyerDreamAgentReplies, housing_agentReplies = get_requirements_recommendations(input)
        #st.write(rawResults)

st.divider()

st.write("Step 2: Enter the house link to check if is dream home")

form1 = st.form(key="form1")
url = form1.text_area("Enter the dream house link", height=20
                        , placeholder="https://www.propnex.com/listing-details/575251/413a-fernvale-link")

if form1.form_submit_button("Submit"):
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
