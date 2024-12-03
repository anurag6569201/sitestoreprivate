import requests
from urllib.parse import urlencode

def RedTubeApiCall(http_server, params=None):
    # Ensure params is a dictionary
    if params is None:
        params = {}

    # Build the query string
    query_string = '?' + urlencode(params)

    # Make the GET request
    response = requests.get(http_server + query_string)

    # Check if the response is successful
    if response.status_code == 200:
        return response.text  # Return the content of the response
    else:
        return None  # Handle failure case if necessary

# Base URL for the RedTube API
http_server = 'https://api.redtube.com/'

# Define the API call and parameters
call = 'redtube.Categories.getCategoriesList'
params = {
    'output': 'xml',
    'data': call
}

# Make the API call
response = RedTubeApiCall(http_server, params)

if response:
    # Handle the response (for example, print the result)
    print(response)
else:
    print("Failed to retrieve data.")
