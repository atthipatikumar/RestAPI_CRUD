from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Details(models.Model):
    Name = models.CharField(max_length=200, verbose_name="Name")
    Address = models.CharField(max_length=250, verbose_name="Address")
    Profile_Picture = models.ImageField()
    Birthdate = models.DateField(null=True, blank=True)
    Years_of_experience = models.IntegerField(null=True, blank=True)
    Preferred_Language = models.CharField(max_length=100, verbose_name="Preferred Language")
    user = models.ForeignKey('User', related_name='user', on_delete=models.PROTECT)

    def __str__(self):
        return self.Name



