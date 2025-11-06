import streamlit as st
from PIL import Image

image = Image.open('pages/streamlit_methodology_flowchart.jpg')

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title(":bar_chart: Methodology")

st.write(":speech_balloon: The flowchart below shows the methodology and data sources that were used to develop the School Navigator Streamlit App. ")

st.image(image, caption='Methodology Flow Chart', use_column_width=True)

with st.expander("How to use this App"):
    st.write("1. Enter your prompt in the chat box on the main page.")
    st.write("2. Click the 'Submit' button.")
    st.write("3. The app will generate an answer based on your query. Do refer to the sample questions on the main page for the types of queries it can be used for :sunny:")