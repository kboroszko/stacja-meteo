from django.db import models
from enum import IntEnum


class Station(models.Model):
    name = models.CharField(max_length=100)


class DataType(IntEnum):
    TEMPERATURE = 1
    PRESSURE = 2
    HUMIDITY = 3

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Record(models.Model):
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    data_type = models.IntegerField(choices=DataType.choices())
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=False, editable=True, null=False, blank=False)

    class Meta:
        unique_together = ('station', 'data_type', 'timestamp')
