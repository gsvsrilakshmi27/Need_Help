# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_database'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Database',
        ),
    ]
