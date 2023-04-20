# create a virtual environment and install the following packages: py-jama-rest-client, python-dotenv
# initialize the virtual environment and run the script with python3 main.py

import os
from py_jama_rest_client.client import JamaClient
from dotenv import load_dotenv
load_dotenv('.env')

# sets python variables to the api instance, client ID and secret. 
# requires a file in the root directory called '.env' with each of the variables defined in it.
# This is to keep sensitive information out of the git repositiory; .env is part of the .gitignore file.
jama_url = os.environ['JAMA_API_URL']
jama_api_username = os.environ['API_CLIENT_ID']
jama_api_password = os.environ['API_CLIENT_SECRET']

# creates a connection object with oauth and the api instance, client id and secret
oauth_client = JamaClient(jama_url, credentials=(jama_api_username, jama_api_password), oauth=True)

# uses the get_projects method in the 
project_list = oauth_client.get_projects()

# Print the data out for each project.
for project in project_list:
    project_name = project['fields']['name']
    print('\n---------------' + project_name + '---------------')

    # Print each field
    for field_name, field_data in project.items():

        # If one of the fields(i.e. "fields") is a dictionary then print it's sub fields indented.
        if isinstance(field_data, dict):
            print(field_name + ':')
            # Print each sub field
            for sub_field_name in field_data:
                sub_field_data = field_data[sub_field_name]
                print('\t' + sub_field_name + ': ' + str(sub_field_data))

        # If this field is not a dictionary just print its field.
        else:
            print(field_name + ': ' + str(field_data))
