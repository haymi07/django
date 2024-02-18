from typing import Any
from django.db import models

# Create your models here.
class Expriance(models.Model):
    text = models.CharField(max_length=100)
    Thumbnail = models.ImageField()
    html_link = models.CharField(max_length=100, null=True)
    def __str__(self) -> str:
        return self.text

class Oldies_Day(models.Model):
    image = models.ImageField()
    text = models.CharField(max_length =100)
    def __str__(self) -> str:
        return self.text

class workers_day(models.Model):
    image = models.ImageField()
    text = models.CharField(max_length =100)
    def __str__(self) -> str:
        return self.text
    
class Culture_Day(models.Model):
    image = models.ImageField()
    text = models.CharField(max_length =100)
    def __str__(self) -> str:
        return self.text
    
class prom(models.Model):
     image = models.ImageField()
     text = models.CharField(max_length =100)
     def __str__(self) -> str:
        return self.text

class Graduation(models.Model):
     image = models.ImageField()
     text = models.CharField(max_length =100)
     def __str__(self) -> str:
        return self.text
     



     class homepage(models.Model):
         image=models.ImageField()
         text= models.CharField(max_length=100)
         def __str__(self) -> str:
           return self.text

