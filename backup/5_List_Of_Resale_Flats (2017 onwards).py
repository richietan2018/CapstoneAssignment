#data source: https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view
import streamlit as st
import pandas as pd
import json

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="List of Resale Flats (2017 onwards)"
)
# endregion <--------- Streamlit App Configuration --------->

#HEADER
st.title("List of Resale Flats (2017 Onwards)")

#BODY
data = pd.read_csv('./data/ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv')
df = pd.DataFrame(data)
df

st.caption("The data is accurate as of 8 October 2024.")

#FOOTER
st.divider()
with st.expander("IMPORTANT NOTICE"):
    st.write("1. This web application is a prototype developed for educational purposes only.")
    st.write("2. The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.")
    st.write("3. Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.")
    st.write("4. Always consult with qualified professionals for accurate and personalized advice.")