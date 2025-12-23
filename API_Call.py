'''
This file is used to create a class that can be used to fetch data from an API. It will be used to fetch data from the API and return it in a structured format. 
It will also be used to handle errors and exceptions that may occur during the API call.
I will use the requests library to make the API call and handle the response. I will also use the json library to parse the response and return it in a structured format.
I will also use the logging library to log the errors and exceptions that may occur during the API call.
I will store the data in a pandas DataFrame and return it. I will also provide a method to save the DataFrame to a CSV file.
I will also provide a method to save the DataFrame to a JSON file. I will also provide a method to save the DataFrame to a Excel file.
I will also provide a method to save the DataFrame to a SQL database. I will use a pandas library to handle the data and the sqlalchemy library to handle the SQL database.
'''

import requests
import json
import pandas as pd
import logging
from sqlalchemy import create_engine


class Input_From_API:
    def __init__(self, url, params=None, headers=None):
        self.url = url
        self.params = params
        self.headers = headers
        self.data = None

    def fetch_data(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers)
            response.raise_for_status()  # Raise an HTTPError if the response status is not 200
            self.data = response.json()  # Parse the JSON response
            return self.data
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching data from API: {e}")
            return None

    def save_to_csv(self, filename):
        if self.data is not None:
            df = pd.DataFrame(self.data)
            df.to_csv(filename, index=False)
        else:
            logging.warning("No data to save to CSV. Please fetch data first.")

    def save_to_json(self, filename):
        if self.data is not None:
            with open(filename, 'w') as f:
                json.dump(self.data, f)
        else:
            logging.warning("No data to save to JSON. Please fetch data first.")

    def save_to_excel(self, filename):
        if self.data is not None:
            df = pd.DataFrame(self.data)
            df.to_excel(filename, index=False)
        else:
            logging.warning("No data to save to Excel. Please fetch data first.")

    def save_to_sql(self, db_url, table_name):
        if self.data is not None:
            df = pd.DataFrame(self.data)
            engine = create_engine(db_url)
            df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        else:
            logging.warning("No data to save to SQL. Please fetch data first.")
            
'''
This class is used to safely request access to a player's account or game data. It will be used to request access to a player's account or game data and return a response in a structured format.
It will also be used to handle errors and exceptions that may occur during the API call. I will use the requests library to make the API call and handle the response. 
I will also use the json library to parse the response and return it in a structured format. I will also use the logging library to log the errors and exceptions that may occur during the API call.
I will store the data in a pandas DataFrame and return it. I will also provide a method to save the DataFrame to a CSV file.
I will also provide a method to save the DataFrame to a JSON file. I will also provide a method to save the DataFrame to a Excel file.
I will also provide a method to save the DataFrame to a SQL database. I will use a pandas library to handle the data and the sqlalchemy library to handle the SQL database.
'''
class RSO:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.access_token = None

    def request_access(self, code):
        try:
            response = requests.post('https://auth.riotgames.com/api/v1/authorization', json={
                'client_id': self.client_id,
                'client_secret': self.client_secret,
                'redirect_uri': self.redirect_uri,
                'grant_type': 'authorization_code',
                'code': code
            })
            response.raise_for_status()
            self.access_token = response.json().get('access_token')
            return self.access_token
        except requests.exceptions.RequestException as e:
            logging.error(f"Error requesting access: {e}")
            return None

    def save_to_csv(self, filename):
        if self.access_token is not None:
            # Assuming the access token can be used to fetch player data
            # and the data is returned in a JSON format
            response = requests.get('https://api.riotgames.com/lol/summoner/v4/summoners/by-name/PlayerName', headers={
                'Authorization': f'Bearer {self.access_token}'
            })
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame([data])
            df.to_csv(filename, index=False)
        else:
            logging.warning("No access token available. Please request access first.")

    def save_to_json(self, filename):
        if self.access_token is not None:
            response = requests.get('https://api.riotgames.com/lol/summoner/v4/summoners/by-name/PlayerName', headers={
                'Authorization': f'Bearer {self.access_token}'
            })
            response.raise_for_status()
            data = response.json()
            with open(filename, 'w') as f:
                json.dump(data, f)
        else:
            logging.warning("No access token available. Please request access first.")

    def save_to_excel(self, filename):
        if self.access_token is not None:
            response = requests.get('https://api.riotgames.com/lol/summoner/v4/summoners/by-name/PlayerName', headers={
                'Authorization': f'Bearer {self.access_token}'
            })
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame([data])
            df.to_excel(filename, index=False)
        else:
            logging.warning("No access token available. Please request access first.")
        
            