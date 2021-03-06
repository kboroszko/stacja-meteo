# Generated by Django 3.1.1 on 2020-10-21 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterUniqueTogether(
            name='record',
            unique_together={('station', 'data_type', 'timestamp')},
        ),
    ]
