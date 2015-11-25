# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_delete_database'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('donar_name', models.CharField(max_length=25)),
                ('blood_group', models.CharField(max_length=20)),
                ('city_name', models.CharField(max_length=20)),
                ('mobile_number', models.BigIntegerField()),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
