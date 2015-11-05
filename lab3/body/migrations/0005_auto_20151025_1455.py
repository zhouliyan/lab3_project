# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0004_auto_20151025_0733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='PublishDate',
            field=models.CharField(max_length=50),
        ),
    ]
