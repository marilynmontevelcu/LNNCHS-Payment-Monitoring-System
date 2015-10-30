# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='id',
        ),
        migrations.AlterField(
            model_name='studentinfo',
            name='student_id',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
    ]
