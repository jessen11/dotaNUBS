from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    primary_attribute = models.CharField(max_length=200)
