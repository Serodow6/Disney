from django.db import models

# Create your models here.


class Parks(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    button = models.CharField(max_length=255)

class Movies(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)

class Wod(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)



class Shows(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()

class Mfdt(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()

class News(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    button = models.CharField(max_length=255)


class Product(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    status = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    rarity = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)

class Familyshows(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()

class Concertandevents(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    description = models.TextField()