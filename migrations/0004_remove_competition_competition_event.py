# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20160121_0511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competition',
            name='competition_event',
        ),
    ]
