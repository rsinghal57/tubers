from django.db import models
from django.db.models.fields import CharField
from datetime import datetime

# Create your models here.
class Hiretuber(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    tuber_id=models.IntegerField(blank=True)
    tuber_name=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    state=models.CharField(max_length=255)
    message=models.TextField(blank=True)
    phone=models.CharField(max_length=255)
    user_id=models.IntegerField(blank=True)
    created_date=models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email


class Contactteam(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    company=models.CharField(max_length=255)
    subject=models.CharField(max_length=255)
    message=models.CharField(max_length=255)
    created_date=models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.name