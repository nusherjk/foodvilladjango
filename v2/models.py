from django.db import models


# Create your models here.
class User (models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=90)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name


class FoodData(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    category = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return self.title

class Complaints(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    complain = models.CharField(max_length=1000)

    def __str__(self):
        return self.email
'''class Cart(models.Model):
    Foodtitile = models.ForeignKey(FoodData.title, on_delete= models.CASCADE)
    '''