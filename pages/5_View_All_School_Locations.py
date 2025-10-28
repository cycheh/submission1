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