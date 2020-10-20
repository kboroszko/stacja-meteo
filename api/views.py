from django.http import HttpResponse
from handlers.data_handler import stations_handler
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the api index.")

#zmiana
# Create your views here.

def get_stations(request):
    dane = stations_handler()
    return JsonResponse(dane)


def get_data(request, station_id):
    # use a handler here
    return HttpResponse(f"stationId:{station_id}\nget data endpoint.")


def post_data(request, station_id):
    # use a handler here
    return HttpResponse(f"stationId:{station_id}\npost data endpoint.")
