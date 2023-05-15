# Generated by Django 3.2.16 on 2023-04-11 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('bike_ID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=30)),
                ('usable', models.BooleanField(default=False)),
                ('location', models.CharField(default='', max_length=30)),
                ('purchase_date', models.DateTimeField()),
            ],
        ),
    ]