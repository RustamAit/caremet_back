from django.db import models
import datetime


class Helper(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    IIN = models.CharField(max_length=300)
    N_Id_number = models.CharField(max_length=200)
    rating = models.FloatField


class HelperRequest(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    IIN = models.CharField(max_length=300)
    N_Id_number = models.CharField(max_length=200)