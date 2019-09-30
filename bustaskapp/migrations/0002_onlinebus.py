# Generated by Django 2.2 on 2019-09-19 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bustaskapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='onlinebus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buscode', models.CharField(max_length=10)),
                ('bustype', models.CharField(max_length=30)),
                ('source', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('departure', models.DateField()),
                ('depature', models.TimeField()),
            ],
        ),
    ]
