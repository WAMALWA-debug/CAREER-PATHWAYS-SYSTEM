from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Prediction(models.Model):
    #student = models.ForeignKey(User, on_delete=models.CASCADE )
    student_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)

    math = models.IntegerField()
    eng = models.CharField()
    kis = models.CharField()
    science = models.CharField()
    pretech = models.CharField()
    agriculture = models.CharField()
    cre = models.CharField()
    carts = models.CharField()
    sst = models.CharField()

    scienceproj = models.IntegerField()
    cartsproj= models.IntegerField()
    agrproj = models.IntegerField()

    prefect = models.IntegerField()
    musicdrama=models.IntegerField()
    sports=models.IntegerField()

    school = models.IntegerField()

    pathway = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name