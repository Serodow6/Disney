from django.db import models

# Create your models here.
class Banner(models.Model):
    image = models.ImageField()

class Parks(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()

class Movies(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)

class Wod(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)

class Mfd(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)

class Shows(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()

class Mfdt(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)

class News(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()

class Shop(models.Model):
    image = models.ImageField()

class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    status = models.CharField(max_length=255)