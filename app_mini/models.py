from django.db import models

# Create your models here.

class login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    user_type = models.CharField(max_length =50)


#used to create table for police_station_registration
class police_station_registration(models.Model):
    station_id = models.CharField(max_length=100, primary_key=True)
    login_id = models.ForeignKey(login, on_delete=models.CASCADE, null=True, blank=True)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100)
    district = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)


# used to create table for staff_registration
class staff(models.Model):
    staff_id = models.CharField(max_length=50, primary_key=True)
    login_id = models.ForeignKey(login, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=20)
