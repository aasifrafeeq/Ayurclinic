# Generated by Django 3.2.6 on 2021-10-06 13:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(default='NIL', max_length=10)),
                ('age', models.PositiveIntegerField()),
                ('diagnosis', models.CharField(default='NIL', max_length=2000)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('price', models.IntegerField()),
                ('users', models.ManyToManyField(blank=True, related_name='users', to='patients.Patient')),
            ],
        ),
    ]
