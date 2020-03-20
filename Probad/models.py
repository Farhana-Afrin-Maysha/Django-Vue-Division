from django.db import models


# from django.utils import timezone
# from django.contrib.auth.models import User


class Division(models.Model):
    name = models.CharField(max_length=25)
    bn_name = models.CharField(max_length=25)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    bn_name = models.CharField(max_length=25)
    lat = models.CharField(max_length=15, null=True)
    lon = models.CharField(max_length=15, null=True)
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    bn_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Chondokotha(models.Model):
    title = models.CharField(max_length=200)
    category = models.ManyToManyField(Category)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def category_name(self):
        return self.category.name

    def district_name(self):
        return self.district.name

    def division_name(self):
        return self.district.division.name

    def __str__(self):
        return self.title


class Place(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Resturant(models.Model):
   place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True )
   serves_hot_dog = models.BooleanField(default=False)
   serves_pizza = models.BooleanField(default=False)

   def __str__(self):
        return self.place.name