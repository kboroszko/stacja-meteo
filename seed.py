import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meteo.settings")
django.setup()

from django_seed import Seed
import random


seeder = Seed.seeder(locale='pl_PL')

from api.models import *

seeder.add_entity(Station, 1, {
    'name': seeder.faker.city(),
})

# inserted_pks = seeder.execute()
# station_id = inserted_pks[Station][0]

seeder = Seed.seeder(locale='pl_PL')

seeder.add_entity(Record, 10, {
    # 'station': Station.objects.filter(id=station_id).first(),
    'data_type': DataType.PRESSURE,
    'value': random.random()
})

seeder.execute()
