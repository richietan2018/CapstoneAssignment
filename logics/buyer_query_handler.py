import os
import openai
import json
import csv
import pandas as pd
from helper_functions import llm
from fuzzywuzzy import fuzz
import pyarrow as pa

#Load the data
data = pd.read_csv('./data/ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv')
df = pd.DataFrame(data)
df 

#Step 1: Idenitify the list of town and flat type first.
def identify_town_flattype(user_message):
    delimiter = "####"

    system_message = f"""
    You will be provided with buyer queries. \
    The buyer query will be enclosed in
    the pair of {delimiter}.

    Decide if the query is relevant to any specific town
    in the Python dataframe below, which each key is a `town`
    with `flat_type`, `block` and `street_name` .

    If there are any relevant town(s) found, output the pair(s) of a) `town` the relevant flat_type and b) the associated `flat_type`, `block` and `street_name`into a
    list of dictionary object, where each item in the list is a relevant town
    and each town is a dictionary that contains two keys:
    1) town
    2) flat_type
    3) block
    4) street_name

    If are no relevant town are found, output an empty list.

    Ensure your response contains only the list of dictionary objects or an empty list, \
    without any enclosing tags or delimiters.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]
    town_and_flattype_response_str = llm.get_completion_by_messages(messages)
    town_and_flattype_response_str = town_and_flattype_response_str.replace("'", "\"")
    town_and_flattype_response = json.loads(town_and_flattype_response_str)
    return town_and_flattype_response

#Step 2: Retrieve the details of the area
def get_town_details(town_n_flattype: list[dict]):
    # Create a new DataFrame for matching rows
    final_list_of_details = pd.DataFrame()

    for x in town_n_flattype:
        townName = x['town'].upper()
        flatType= x['flat_type'].upper()
        block =x['block'].upper()
        streetName =x['street_name'].upper()

    try:
        final_list_of_details = df[
            (df['town'] == townName) &
            (df['flat_type'] == flatType) &
            (df['block'] == block) &
            (df['street_name'].apply(lambda x: fuzz.partial_ratio(x.upper(), streetName.upper()) > 90))  # Similar match
        ]
    except UnboundLocalError:
        print("Error: 'townName' is not defined. Please ensure it is initialized before use.")

    # Ensure the DataFrame columns are compatible with Arrow
    for col in final_list_of_details.columns:
        if final_list_of_details[col].dtype == 'object':
            final_list_of_details[col] = final_list_of_details[col].astype(str)
        elif pd.api.types.is_numeric_dtype(final_list_of_details[col]):
            final_list_of_details[col] = final_list_of_details[col].astype(float)  # or int if applicable

    #To reset the index of the dataframe
    final_list_of_details.reset_index(drop=True, inplace=True)

    # Attempt to convert to Arrow Table
    try:
        arrow_table = pa.Table.from_pandas(final_list_of_details)
        print("Conversion to Arrow table successful!")
    except Exception as e:
        print(f"Error converting to Arrow table: {e}")

    return final_list_of_details

#Step 3: Generate the response based on the details given
def generate_response_based_on_result_details(user_message, result_details):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the customer queries.
    The customer query will be delimited with a pair {delimiter}.

    Step 1:{delimiter} If the user is asking about area of stay and flat type, \
    understand the relevant area of stay and flat type from the following list.
    All available area of stay and flat type shown in the data below:
    {result_details}

    Step 2:{delimiter} Use the information about the area of stay and flat type, to \
    generate the answer for the customer's query.
    You must only rely on the facts or information in the list provided.
    Your response should be as detail as possible and \
    include information that is useful for buyer to better understand the area and room of stay.

    Step 3:{delimiter}: Answer the customer in a friendly and professional tone and is mandatory to have an output.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    the buyer to make their decision.
    Complete with details such pricing, storey comparision, lease_commence_date.
    Use Neural Linguistic Programming to construct your response.

    Use the following format:
    Step 1:{delimiter} <step 1 reasoning>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to buyer>

    Make sure to include {delimiter} to separate every step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_message}{delimiter}"},
    ]

    response_to_buyer = llm.get_completion_by_messages(messages)
    response_to_buyer = response_to_buyer.split(delimiter)[-1]
    return response_to_buyer

#Main Function 
def process_buyer_message(user_input):
    delimiter = "```"

    # Process 1: If details are found, look them up
    town_n_flattype = identify_town_flattype(user_input)
    print("town_n_flattype : ", town_n_flattype)
    
    # Process 2: Get the list of areas with Details
    result_details = get_town_details(town_n_flattype)

    # Process 3: Generate Response based on Course Details
    reply = generate_response_based_on_result_details(user_input, result_details)
    print(reply)
    
    if reply == "" and result_details == "":
        reply="Your question is invalid for our discussion here. Kindly ask questions related to resale housing."
    
    #return result_details
    return reply, result_details