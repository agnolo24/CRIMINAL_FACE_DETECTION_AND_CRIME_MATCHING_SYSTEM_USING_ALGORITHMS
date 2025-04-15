from django.utils import timezone
from django.db import models

# Create your models here.

class login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length =50)
    varification_status = models.CharField(default='pending', max_length=20)

class police_station_registration(models.Model):
    station_id = models.CharField(max_length=100, primary_key=True)
    login_id = models.ForeignKey(login, on_delete=models.CASCADE, null=True, blank=True)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)

    def __str__(self):
        return (self.station_id)


class user_registration(models.Model):
    login_id = models.ForeignKey(login, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=30)
    contact = models.CharField(max_length=20)


class Enquiry(models.Model):
    user_id = models.ForeignKey(user_registration, on_delete=models.SET_NULL, null=True)
    station_id = models.ForeignKey(police_station_registration, on_delete=models.SET_NULL, null=True)
    enquiry_data = models.TextField()
    date = models.DateField(auto_now_add=True, null=True)
    reply = models.TextField(null = True)


class staff(models.Model):
    staff_id = models.CharField(max_length=50, primary_key=True)
    login_id = models.ForeignKey(login, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=20)
    station = models.ForeignKey(police_station_registration, on_delete=models.SET_NULL, null=True)


class Petition(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL, null=True)
    station = models.ForeignKey(police_station_registration, on_delete=models.SET_NULL, null=True)
    petition_text = models.TextField()
    date = models.DateField(auto_now_add=True)
    reply = models.TextField(null = True)