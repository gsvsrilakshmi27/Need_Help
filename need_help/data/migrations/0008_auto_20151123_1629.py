# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_database'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Database',
            new_name='Database1',
        ),
    ]
