# Generated by Django 2.2 on 2019-09-20 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bustaskapp', '0002_onlinebus'),
    ]

    operations = [
        migrations.CreateModel(
            name='seat2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seatnumber', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('BUSNUMBER', models.CharField(max_length=30)),
                ('BUSTYPE', models.CharField(max_length=30)),
                ('SOURCE', models.CharField(max_length=40)),
                ('DESTINATION', models.CharField(max_length=30)),
                ('DEPARTURE', models.DateField()),
                ('DEPATURE', models.TimeField()),
            ],
        ),
    ]
