# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_auto_20151123_1630'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Database',
        ),
    ]
