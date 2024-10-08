from django.db import models
from django.db.models import CharField, IntegerField, TextField


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    guest_number = models.IntegerField()
    comment = models.CharField(max_length=1000)

    def __str__(self):
        return self.first_name + " " + self.last_name


# Add code to create Menu model
class Menu(models.Model):
    name = CharField(max_length=200)
    price = IntegerField()
    menu_item_description = TextField(max_length=1000, default="")

    def __str__(self) -> str:
        return self.name
