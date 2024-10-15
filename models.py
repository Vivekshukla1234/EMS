from django.db import models

# Create your models here.

class Employee22(models.Model):

    #eid=models.IntegerField()
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=20)

    def __str__(self):
        return self.name
