from api.models import Station


def stations_handler():
    stacje = {}
    for o in Station.objects.all():
       stacje[o.name] = o.id
    return stacje

def rekord_handler():
    pass