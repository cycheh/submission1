import streamlit as st
import pandas as pd
import json

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title(":books: Dataset on School Subjects")

# Load the JSON file

with open('./data/transformed_subjects.json', 'r') as file:
    json_string = file.read()
    subjects_dict = json.loads(json_string)
    print(subjects_dict)

list_of_dict = []
for school_name, details_dict in subjects_dict.items():
    list_of_dict.append(details_dict)

# display the `dict_of_course` as a Pandas DataFrame
df = pd.DataFrame(list_of_dict)
df

st.write(":woozy: Oops, the dataset may be too big to be viewed in this page. You can access the original data source using the below link!")

st.write("Source: Ministry of Education. (2017). Subjects Offered (2025) [Dataset]. data.gov.sg.")

st.link_button("Access the Subjects Offered dataset here", "https://data.gov.sg/datasets?topics=education&resultId=d_f1d144e423570c9d84dbc5102c2e664d&page=1")