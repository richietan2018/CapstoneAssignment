#data source: https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view
import streamlit as st
import pandas as pd
import numpy as np
from logics.buyer_query_handler import process_buyer_message
from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Enquiry on resale flat pricing and records"
)
# endregion <--------- Streamlit App Configuration --------->

tab1, tab2 = st.tabs(["Enquiry on resale flat pricing and records", "Resale Flat Data"])
#Tab 1: Enquiry on resale flat pricing and records

with tab1:
    #Page Title
    st.title("Enquiry on resale flat pricing and records")

    #
    form = st.form(key="form")
    user_prompt = form.text_area("Enter your enquires here", height=200, help="Mandatory Details: Town Name, Block No, Street Name, Flat Type"
                                , placeholder="Kindly provide 5 details and recommendation on the resale flat pricing for a 4 room flat in Woodlands Dr 42, Block 604 in Woodlands ?")
    #I am looking for a resale flat, 5 room in Sengkang , Anchorvale Dr , 301D. Kindly provide some details on this.

    if form.form_submit_button("Submit"):
        st.toast(f"Your input - {user_prompt} as been submitted. Please give us a moment.")
        st.divider()
        response,town_details = process_buyer_message(user_prompt)
        st.write(response)

        st.divider()
        df = pd.DataFrame(town_details)
        df 
        
        st.divider()
        chart_data = pd.DataFrame(df, columns=["month", "resale_price"])
        st.line_chart(
            chart_data,
            x="month",
            y="resale_price",
        ) 

with tab2: 
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
