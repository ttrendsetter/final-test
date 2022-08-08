import sqlalchemy
import requests
import json



#X-Yandex-API-Key: ba7a3712-6158-4598-87c0-df60309ab428
def parse():
    data = []

    for _ in range(100):
        response = requests.get('')
        result = response.text

