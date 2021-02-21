from api.models import Station, Record, DataType
import random
from datetime import datetime, timezone, timedelta

def stations_handler():
    stacje = {}
    for o in Station.objects.all():
       stacje[o.name] = o.id
    return stacje


def get_rekords_handler(station_id, date_from, date_to, data_type):
    s = Station.objects.get(id=station_id)
    records = list(Record.objects.filter(data_type=data_type, timestamp__gt=date_from,
                                         timestamp__lt=date_to, station=s).all())
    ret = {}
    for r in records:
        ret[str(r.timestamp)] = r.value
    return ret


def data_type_str_to_int_handler(data_type_name):
    return DataType[data_type_name]


def post_handler(station_id,data_type,value,timestamp):
    s = Station.objects.get(id = station_id)
    r = Record(Station=s, data_type=data_type , value = value,
               timestamp=timestamp)
    r.save()


