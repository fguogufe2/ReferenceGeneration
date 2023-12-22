import requests

"""
Crossref API call is free and does not require an API key.
"""

def api_call_doi(entry, row=1):
    # Define the URL for the Crossref API
    url = "http://api.crossref.org/works"

    # Define the parameters for your query; the rows determine how many results you get back;
    # for highly detailed and refined queries, one is enough. 
    params = {
        "query.bibliographic": entry,
        "rows": row
    }

    # Make the GET request
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response to JSON
        data = response.json()

        # Process the data as needed (for example, print it)
#         print(data)
    else:
        data = None
        print(f"Failed to retrieve data: {response.status_code}")
        
    return (entry, data['message']['items'][0]['DOI'])


def api_call_bibtex(doi):

    """ the returned data is a string of bibtex"""
    url_parent = "https://api.crossref.org/works/"
    url_suffix = "/transform/application/x-bibtex"

    url =f"{url_parent}{doi}/{url_suffix}"

    response= requests.get(url)
    
    if response.status_code == 200:
        data = response.text
    else:
        data = None
        print(f"Failed to retrieve data: {response.status_code}")

    return data

def write_bibtex(data, file_name):
    """ write the bibtex to a file"""
    with open(f"{file_name}.bib", "w") as f:
        f.write(data)
