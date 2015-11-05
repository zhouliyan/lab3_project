# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0003_auto_20151025_0732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Name', models.CharField(max_length=50)),
                ('Age', models.IntegerField()),
                ('Country', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='AuthorID',
            field=models.ForeignKey(blank=True, to='body.Author', null=True),
        ),
    ]
