from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Package(models.Model):

    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    recipent_name = models.CharField(max_length=45, blank = False)
    recipent_surname = models.CharField(max_length=45, blank= False)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=100)
    apartment_number = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    is_fragile = models.BooleanField(default=False)
    is_prior = models.BooleanField(default=False)

    def recipent_full_name(self):
        recipent_full_name = self.recipent_name + " " + self.recipent_surname
        return recipent_full_name

    def recipent_address(self):
        if self.apartment_number :
            recipent_address = "Street: " + self.street + " " + self.house_number + "/" + self.apartment_number + "/n" + self.city + "/n" + self.region +"/n" + self.country
            return recipent_address
        else :
            recipent_address = "Street: " + self.street + " " + self.house_number + "/n" + self.city + "/n" + self.region + "/n" + self.country
            return recipent_address

    def delivery_sticker(self):
        delivery_sticker =  self.recipent_full_name() + "/n" + self.recipent_address()
        return delivery_sticker