import streamlit as st
import pandas as pd
import json


# Load the JSON file

with open('./data/transformed_address.json', 'r') as file:
    json_string = file.read()
    location_dict = json.loads(json_string)
    print(location_dict)

list_of_dict = []
for school_name, details_dict in location_dict.items():
    list_of_dict.append(details_dict)

# display the `dict_of_course` as a Pandas DataFrame
df = pd.DataFrame(list_of_dict)
df

st.write("Source: Ministry of Education. (2017). General information of schools (2025) [Dataset]. data.gov.sg.")

st.link_button("Access the General Information dataset here", "https://data.gov.sg/datasets?topics=education&resultId=d_688b934f82c1059ed0a6993d2a829089&page=1")