# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-04 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('requisitos', models.ManyToManyField(to='grade.Disciplina')),
            ],
        ),
    ]
