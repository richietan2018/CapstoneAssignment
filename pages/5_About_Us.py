import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="About Us"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About Us")

#Project Scope
st.subheader("**Project Scope**")
st.markdown("This project focuses on creating a centralized platform for HDB resale flats, addressing the challenges of accessing information from multiple sources. It aims to provide practical tips on the resale flat purchasing process (with/without agent) and insights into the market trends in the selected areas. Additionally, the platform feature a user-friendly tool that allows users to quickly determine if a property meets the buyer criteria in just a few steps.")
st.divider()

#Objectives
st.subheader("**Objectives**")
st.markdown("The main objectives is to allow buyer to use the site as an centralized platform which is ease of use to resolve the issues of what the are the benefits or steps between having an agent and not having an agent for resale flat purchases. In addition, with the use of AI how can it assist in the recommendation, findings of historical records and trends. Lastly, how AI can assist in checking if the criteria of the buyer is met by just simply in a few steps which can save time.")
st.divider()

#Data Source
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

#Features
st.subheader("Features")
st.markdown("**Use Case 1**: Simple enquiry on process of purchasing resale flat")
st.markdown("This feature allow the buyer to generate a short useful summary (contains of steps) on how he/she can make a resale flat purchase with/without an agent in just a click.")

st.markdown("**Use Case 2**: Enquiry on resale flat pricing and records")
st.markdown("This feature allow the buyer to generate a summary on the flat he/she have entered in the textbox (townname, streetname, block no and room type). The feature also return the list of records in which related to the buyer input, a line graph is also generated to seek as an comparision on the price of the house over the period of time. This provides an useful insights on how the price of the house is like over the years and hopefully can assist in making the decision if they should purchase the flat.")

st.markdown("**Use Case 3:** Requirements and recommendation")
st.markdown("This feature allow the buyer to make a comparision between it criteria for their dream house with an existing posting online. This feature contains only three simple steps (a) Upload/Enter Criteria, (b) Enter the Posting Link, (c) Enter the inputs, to make the checks instead of going through it either by eyeballing of comparing using excel which can potientially save some time.")