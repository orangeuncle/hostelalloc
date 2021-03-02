from django.db import models
from django.utils import timezone

# Create your models here.


class Student(models.Model):
    name = models.TextField()
    regNo = models.CharField(max_length=12)
    sex = models.TextField(default='')
    hostel = models.IntegerField(default=0)
    room = models.IntegerField(default=0)
    date_payed = models.DateTimeField(default=timezone.now)

    def __str__(self):
        name = self.name
        regNo = self.regNo
        date_payed = self.date_payed
        text = name+ " - "+ regNo+ " "+ str(date_payed)
        return text


class Hostel(models.Model):
    hostel_id = models.IntegerField()
    name = models.TextField(default='')
    gender = models.CharField(max_length=1)
    rooms = models.IntegerField(default=0)
    room_size = models.IntegerField(default=0)

    def __str__(self):
        name = self.name
        return name + " hostel"