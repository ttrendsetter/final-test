from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.parsing, name='parser'),
    path('data', csrf_exempt(views.DbData.as_view()), name='data')
]