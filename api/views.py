from django.http import HttpResponse, HttpResponseServerError
from handlers.data_handler import stations_handler, get_rekords_handler, data_type_str_to_int_handler
from django.http import JsonResponse
import sys

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

#zmiana
# Create your views here.

def get_stations(request):
    dane = stations_handler()
    return JsonResponse(dane)


def get_data(request, station_id):
    date_from = request.GET.get('from')
    if not date_from:
        raise Exception()
    date_to = request.GET.get('to')
    if not date_to:
        raise Exception()
    data_type = data_type_str_to_int_handler(request.GET.get('data_type'))
    dane = get_rekords_handler(station_id, date_from, date_to, data_type)
    return JsonResponse(dane, safe=False)


def post_data(request, station_id):
    # use a handler here
    return HttpResponse(f"stationId:{station_id}\npost data endpoint.")
