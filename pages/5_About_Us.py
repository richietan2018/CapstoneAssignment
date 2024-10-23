import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="About Us"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About Us")

st.subheader("**Project Scope**")
st.markdown("This project focuses on creating a centralized platform for HDB resale flats, addressing the challenges of accessing information from multiple sources. It aims to provide practical tips on the resale flat purchasing process (with/without agent) and insights into the market trends in the selected areas. Additionally, the platform will feature a user-friendly tool that allows users to quickly determine if a property meets the buyer criteria in just a few clicks.")
st.divider()
st.subheader("**Objectives**")
st.divider()
st.subheader("**Data Source**")
st.markdown("")
st.markdown("**Use Case 1**: Simple enquiry on process of purchasing resale flat")
st.markdown("1. A Step-by-step Guide to Buy HDB Resale Flat in 2024")
st.markdown("Link: https://ohmyhome.com/en-sg/blog/timeline-buying-hdb-resale-flat-hdb-resale-procedure")
st.markdown("2. How to Buy an HDB Resale Flat Without an Agent And Save on Fees in 2024: A Step-by-Step Guide")
st.markdown("Link: https://blog.seedly.sg/buy-a-hdb-resale-flat-without-an-agent/")
st.markdown("")

st.markdown("**Use Case 2:** Enquiry on resale flat pricing and records")
st.markdown("1. Resale flat prices based on registration date from Jan-2017 onwards")
st.markdown("Link: https://data.gov.sg/datasets/d_8b84c4ee58e3cfc0ece0d773c8ca6abc/view")
st.markdown("")

st.markdown("**Use Case 3:** Requirements and recommendation")
st.markdown("1. Depends on user input- eg. Propnex site, other site do not allow the retrieve of data.")
st.divider()
st.subheader("Features")
