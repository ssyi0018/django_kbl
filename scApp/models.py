from django.db import models


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()
    notes = models.CharField(max_length=200, null=True, blank=True)


class Department(models.Model):
    title = models.CharField(max_length=20)


class Role(models.Model):
    caption = models.CharField(max_length=16)
