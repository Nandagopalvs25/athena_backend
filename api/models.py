from django.db import models

# Create your models here.

class Events(models.Model):
    name=models.CharField(max_length=200)
    details=models.CharField(max_length=500)
    date = models.DateField()
    price=models.IntegerField()
  
    def __str__(self):
        return self.name
  

class Posters(models.Model):
    event=models.ForeignKey(Events,related_name='posters',on_delete=models.CASCADE)
    link=models.CharField()

    def __str__(self):
        return self.link

class Coordinators(models.Model):
    event=models.ForeignKey(Events,related_name='cords',on_delete=models.CASCADE)
    cord_name=models.CharField(max_length=200)
    cord_num=models.CharField()

    def __str__(self):
        return self.cord_name
