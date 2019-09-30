from django.db import models

class registration(models.Model):
    userid=models.IntegerField(primary_key=True)
    fullname=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    email=models.EmailField()
    membership=models.CharField(max_length=20)
    mobile=models.CharField(max_length=10)


class onlinebus(models.Model):
    buscode=models.CharField(max_length=10)
    bustype=models.CharField(max_length=30)
    source=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    departure=models.DateField()
    depature=models.TimeField()


class seat2(models.Model):

    seatnumber=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    BUSNUMBER=models.CharField(max_length=30)
    BUSTYPE=models.CharField(max_length=30)
    SOURCE=models.CharField(max_length=40)
    DESTINATION=models.CharField(max_length=30)
    DEPARTURE=models.DateField()
    DEPATURE=models.TimeField()
