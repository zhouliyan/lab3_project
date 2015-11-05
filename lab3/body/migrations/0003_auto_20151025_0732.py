# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0002_auto_20151025_0650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='AuthorID',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
    ]
