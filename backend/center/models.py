from django.db import models

class center(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=20)
    region = models.CharField(max_length=20)

class owner(models.Model):
    id = models.IntegerField(primary_key=True)
    des = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    place = models.CharField(max_length=20)

class registration(models.Model):
    id = models.IntegerField(primary_key=True)
    plate = models.CharField(max_length=20, unique=True)
    reg_date = models.DateField()
    place = models.CharField(max_length=20)
    car_des = models.CharField(max_length=200)
    purpose = models.CharField(max_length=20)
    owner_id = models.ForeignKey(owner, on_delete=models.CASCADE)

class inspection(models.Model):
    id = models.IntegerField(primary_key=True)
    insp_date = models.DateField()
    exp_date = models.DateField()
    center_id = models.ForeignKey(center, on_delete=models.CASCADE)
    reg_id = models.ForeignKey(registration, on_delete=models.CASCADE)

# class account(models.Model):
#     id = models.IntegerField(primary_key=True)
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=20)
#     role = models.CharField(max_length=10)
from django.contrib.auth.hashers import make_password

class account(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128)
    place = models.CharField(max_length=20)
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(account, self).save(*args, **kwargs)
