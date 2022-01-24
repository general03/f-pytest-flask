import requests

def get_api_url():
    response = requests.get('https://random-d.uk/api/random')
    return response.url