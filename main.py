# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
from helper_functions import llm
from logics.school_query_handler import process_user_message

from helper_functions.utility import check_password  
    
# Check if the password is correct.  
if not check_password():  
    st.stop()


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Streamlit App")

with st.expander(":mag_right: Disclaimer"):
    st.write("IMPORTANT NOTICE: This web application is a prototype developed for educational purposes only.")

    st.write("The information provided here is NOT intended for real-world usage and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.")

    st.write("Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.")

    st.write("Always consult with qualified professionals for accurate and personalized advice.")
    

form = st.form(key="form")
form.subheader("Prompt")

user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    response = process_user_message(user_prompt)
    st.write(response)

