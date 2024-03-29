from django.db import models
from django.utils import timezone

# Create your models here.


class Student(models.Model):
    name = models.TextField()
    regNo = models.CharField(max_length=24)
    # sex = models.TextField(default='')
    hostel = models.CharField(max_length=100)
    room = models.IntegerField(default=0)
    date_payed = models.DateTimeField(default=timezone.now)
    allocated = models.IntegerField(default=0)

    def __str__(self):
        name = self.name
        regNo = self.regNo
        room = str(self.room)
        hostel = self.hostel.upper()
        date_payed = self.date_payed
        text = regNo+ '  -  '+ name+ " - [%s HOSTEL | ROOM %s]" %(hostel, room)
        return text


class Hostel(models.Model):
    hostel_id = models.IntegerField()
    name = models.TextField(default='')
    gender = models.CharField(max_length=1)
    rooms = models.IntegerField(default=0)
    room_size = models.IntegerField(default=0)
    roomBaseSize = models.IntegerField(default=0)
    # roomBaseNum = models.IntegerField(default=0)

    def __str__(self):
        name = self.name
        return name + ' hostel'