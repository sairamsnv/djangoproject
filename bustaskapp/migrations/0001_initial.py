# Generated by Django 2.2 on 2019-09-18 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('membership', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
    ]