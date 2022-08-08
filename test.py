import requests
import json
def parse():
    headers = {'X-Yandex-API-Key': 'ba7a3712-6158-4598-87c0-df60309ab428'}
    print(f'https://api.weather.yandex.ru/v2/forecast?lat=55.7522&lon=37.6156')
    response = requests.get(f'https://api.weather.yandex.ru/v2/forecast?lat=55.7522&lon=37.6156&limit=7',
                            headers=headers)
    res = json.loads(response.text)
    for day in res['forecasts']:
        print(day['date'], day['parts']['day']['temp_avg'])
parse()