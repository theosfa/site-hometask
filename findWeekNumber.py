import requests
import json

def weekNumber():
    url = 'http://journal.bsuir.by/api/v1/week'
    r = requests.get(url).json()
    return r
