# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0005_auto_20151025_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Price',
            field=models.CharField(max_length=50),
        ),
    ]
