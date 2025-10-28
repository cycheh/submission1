import os
import json
import openai
from helper_functions import llm
import pandas as pd

# Get the list of unique schools in the MOE datasets
df_subjects = pd.read_csv("./data/moe_subjects.csv")
list_of_schools = df_subjects['SCHOOL_NAME'].unique().tolist()

# Create the dictionary with the query category and school name
schools_dict = {
    'Location_and_contact': list_of_schools,
    'Subjects': list_of_schools,
    'Co-curricular_activity_or_CCA': list_of_schools
}

# Define the identify_category_and_school function so that we can retrieve the details from the corresponding dicts later

def identify_category_and_school(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with customer service queries. \
    The customer service query will be enclosed in
    the pair of {delimiter}.

    Decide if the query is relevant to any specific courses
    in the Python dictionary below, which each key is a `category`
    and the value is a list of `school_name`.

    If there are any relevant school name(s) found, output the pair(s) of a) `school_name` which names the relevant schools and b) the associated `category` into a
    list of dictionary object, where each item in the list is a relevant school
    and each school is a dictionary that contains two keys:
    1) category
    2) school_name

    {schools_dict}

    If are no relevant courses are found, output an empty list.

    Ensure your response contains only the list of dictionary objects or an empty list, \
    without any enclosing tags or delimiters.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    category_and_school_response_str = llm.get_completion_from_messages(messages)
    category_and_school_response_str = category_and_school_response_str.replace("'", "\"")
    category_and_school_response = json.loads(category_and_school_response_str)
    return category_and_school_response
    
# Load in the json dicts containing details about school location, subjects offered and CCAs offered

with open('./data/transformed_address.json', 'r') as file:
    json_string = file.read()
    location_dict = json.loads(json_string)

with open('./data/transformed_subjects.json', 'r') as file:
    json_string = file.read()
    subject_dict = json.loads(json_string)

with open('./data/transformed_cca.json', 'r') as file:
    json_string = file.read()
    cca_dict = json.loads(json_string)

# Define the extract_details function to retrieve the details about school location, subjects offered and CCAs offered with the school name(s) entered in the user query

def extract_details(items, location_data, subjects_data, cca_data):
    combined_data = {}
    
    for item in items:
        school_name = item['school_name']
        category = item['category']
        
        # Initialize school entry if not exists
        if school_name not in combined_data:
            combined_data[school_name] = {}
        
        # Look up data based on category
        if category == 'Location_and_contact':
            if school_name in location_data:
                # Extract all location columns
                school_location = location_data[school_name]
                combined_data[school_name]['location_and_contact'] = {
                    'address': school_location.get('address', 'N/A'),
                    'postal_code': school_location.get('postal_code', 'N/A'),
                    'telephone': school_location.get('telephone', 'N/A'),
                    'mrt_station': school_location.get('mrt_station', 'N/A')
                }
            else:
                combined_data[school_name]['location_and_contact'] = "Data not found"
                
        elif category == 'Subjects':
            if school_name in subjects_data:
                combined_data[school_name]['subjects'] = subjects_data[school_name]
            else:
                combined_data[school_name]['subjects'] = "Data not found"

        elif category == "Co-curricular_activity_or_CCA":
            if school_name in cca_data:
                combined_data[school_name]['cca'] = cca_data[school_name]
            else:
                combined_data[school_name]['cca'] = "Data not found"
    
    return combined_data

# Define the generate_response_based_on_school_details function for the LLM to craft a response to the user, with reference to the detailed school info found in the json dicts.

def generate_response_based_on_school_details(user_message, school_details):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the customer queries.
    The customer query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} If the user is asking about school details, \
    understand the relevant school details in the dict below.
    {school_details}

    Step 2:{delimiter} Use the information about the school details to \
    generate the answer for the customer's query.
    Complete with details such as location, contact information, mrt stations, subjects offered and CCA offered etc.
    Take note especially for the subjects offered. If there are certain subjects present in the {school_details} dict that the customer asked about, you need to tell the customer.
    Take note especially for the co-curricular activities or cca offered. If there are certain cca present in the {school_details} dict that the customer asked about, you need to tell the customer.
    You must only rely on the facts or information in the school details.
    Your response should be as detailed as possible and \
    include information that is useful for customer to better understand the school.

    Step 3:{delimiter}: Answer the customer in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    the customers to make their decision.
    Complete with details such as location, contact information, mrt stations, subjects and CCA offered etc. 
    Take note especially for the subjects offered. If there are certain subjects present in the {school_details} dict that the customer asked about, you need to tell the customer.
    Take note especially for the co-curricular activities or cca offered. If there are certain cca present in the {school_details} dict that the customer asked about, you need to tell the customer.
    Use Neural Linguistic Programming to construct your response.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to customer>

    Make sure to include {delimiter} to separate every step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_customer = llm.get_completion_from_messages(messages)
    response_to_customer = response_to_customer.split("Step 3:####")[1].split("####")[0].strip()
    return response_to_customer


# Define the final process_user_message function to run the commands sequentially

def process_user_message(user_input):
    delimiter = "```"

    # Process 1: If schools are found in the user query, look them up in the category and school name dict
    category_and_school_name = identify_category_and_school(user_input)
    print("category and school name : ", category_and_school_name)

    # Process 2: Get the Course Details
    school_details = extract_details(category_and_school_name, location_dict, subject_dict, cca_dict)

    # Process 3: Generate Response based on Course Details
    reply = generate_response_based_on_school_details(user_input, school_details)


    return reply