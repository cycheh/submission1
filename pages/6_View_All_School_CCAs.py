import streamlit as st
import pandas as pd
import json


# Load the JSON file

with open('./data/transformed_cca.json', 'r') as file:
    json_string = file.read()
    cca_dict = json.loads(json_string)
    print(cca_dict)

list_of_dict = []
for school_name, details_dict in cca_dict.items():
    list_of_dict.append(details_dict)

# display the `dict_of_course` as a Pandas DataFrame
df = pd.DataFrame(list_of_dict)
df