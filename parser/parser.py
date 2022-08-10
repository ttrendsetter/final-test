from .models import Towns, Weather
import requests
import json
def parse():
    headers = {'X-Yandex-API-Key': 'ba7a3712-6158-4598-87c0-df60309ab428'}
    Weather.objects.all().delete()
    data = Towns.objects.all()
    for town in data:
        response = requests.get(f'https://api.weather.yandex.ru/v2/forecast?lat={town.lat}&lon={town.lon}&limit=7',
                            headers=headers)
        res = json.loads(response.text)
        temps = [Weather(town_id=town.id, date=day['date'], temp=day['parts']['day']['temp_avg']) for day in res['forecasts']]
        Weather.objects.bulk_create(temps)