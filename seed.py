import os, django
from datetime import datetime, timezone, timedelta
from django_seed import Seed
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meteo.settings")
django.setup()

from api.models import *

seeder = Seed.seeder(locale='pl_PL')

if Station.objects.filter(id=1).exists():
    s = Station.objects.get(id=1)
else:
    s = Station(name=seeder.faker.city())
    s.save()

start_date = datetime.utcnow() - timedelta(days=1)

for i in range(100):
    ts = start_date + i * timedelta(minutes=1)
    r = Record(station=s, data_type=DataType.PRESSURE, value=random.random() * 15,
               timestamp=ts.astimezone(tz=timezone.utc))
    r.save()
