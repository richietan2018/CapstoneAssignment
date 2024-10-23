import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Methodology"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Methodology")

st.subheader("Use Case 1: Simple enquiry on process of purchasing resale flat")
st.image("images/UseCase1.jpg", caption="Use Case 1 Methodology")
st.divider()

st.subheader("**Use Case 2:** Enquiry on resale flat pricing and records")
st.image("images/UseCase2.jpg", caption="Use Case 2 Methodology")
st.divider()

st.subheader("**Use Case 3:** Requirements and Recommendation")
st.image("images/UseCase3.jpg", caption="Use Case 3 Methodology")
st.divider()