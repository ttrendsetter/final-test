from django.http import HttpResponse, JsonResponse
from django.utils.timezone import now
from django.views.generic import View
import json
from .parser import parse
from .models import Weather, Towns
import datetime

# Create your views here.


def parsing(request):
    parse()
    return HttpResponse('Parsing is finished')


class DbData(View):

    def get(self, request):
        return HttpResponse('Please use method POST')

    def post(self, request):
        data = request.body.decode('utf-8')
        data = json.loads(data)
        if data.get('start_date') is None:
            start_date = now()
        else:
            start_date = data.get('start_date')
        if data.get('end_date') is None:
            end_date = now() + datetime.timedelta(days=10)
        else:
            end_date = data.get('end_date')
        towns = Towns.objects.all()
        weather = Weather.objects.filter(date__gte=start_date, date__lte=end_date)
        res = {town.name: [{'temp': temp.temp, 'date': temp.date} for temp in weather if temp.town_id == town.id] for town in towns}
        return JsonResponse(res)

