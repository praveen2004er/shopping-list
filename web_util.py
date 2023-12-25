import requests
import random
import time

def get_json_response(url):
    rate_limit() #TODO - improve this code
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            json_response = response.json()
            return json_response
        else:
            print(f"Error: Unable to fetch JSON response. Status Code: {response.status_code}")
            return None

    except requests.RequestException as e:
        print(f"Error: {e}")
        return None

def rate_limit():
  delay_milliseconds = 1000 
  offset = random.randint(500, 1000)
  time.sleep((delay_milliseconds+offset) / 1000)  # Convert milliseconds to seconds

def dict_to_query_params(params_dict):
    params_list = [f"{key}={value}" for key, value in params_dict.items()]
    return "&".join(params_list)