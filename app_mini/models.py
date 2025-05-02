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
    profile_picture = models.ImageField(upload_to='profile/', null=True)
    login_id = models.ForeignKey(login, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=30)
    contact = models.CharField(max_length=20)
    address = models.TextField(null=True)



class Enquiry(models.Model):
    user_id = models.ForeignKey(user_registration, on_delete=models.SET_NULL, null=True)
    station_id = models.ForeignKey(police_station_registration, on_delete=models.SET_NULL, null=True)
    enquiry_data = models.TextField()
    date = models.DateField(auto_now_add=True, null=True)
    reply = models.TextField(null = True)


class staff(models.Model):
    DESIGNATION_CHOICE = [
        ('DGP', 'Director General of Police'),
        ('IGP', 'Inspector General of Police'),
        ('SP', 'Superintendent of Police'),
        ('DSP', 'Deputy Superintendent of Police'),
        ('CI', 'Circle Inspector'),
        ('SI', 'Sub Inspector'),
        ('ASI', 'Assistant Sub Inspector'),
        ('HC', 'Head Constable'),
        ('PC', 'Police Constable')
    ]
    profile_picture = models.ImageField(upload_to='profile_staff/', null=True)
    staff_id = models.CharField(max_length=50, primary_key=True)
    login_id = models.ForeignKey(login, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICE)
    gender = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=20)
    station = models.ForeignKey(police_station_registration, on_delete=models.SET_NULL, null=True)


class Petition(models.Model):
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL, null=True)
    station = models.ForeignKey(police_station_registration, on_delete=models.SET_NULL, null=True)
    fir_number = models.CharField(max_length=20, null=True)
    petition_text = models.TextField()
    date = models.DateField(auto_now_add=True)
    reply = models.TextField(null = True)


class CriminalRegistration(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    full_name = models.CharField(max_length=30)
    dob = models.DateField()
    case = models.TextField()
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null = True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    photo = models.ImageField(upload_to='criminal_photo/', null=True)
    station = models.ForeignKey(police_station_registration, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)


class FIR(models.Model):
    fir_number = models.CharField(max_length=20, unique=True)
    police_station = models.ForeignKey(police_station_registration, on_delete=models.SET_NULL, null=True)
    petitionInfo = models.ForeignKey(Petition, on_delete=models.SET_NULL, null=True)
    complainant_name = models.CharField(max_length=100)
    complainant_address = models.TextField()
    complainant_contact = models.CharField(max_length=15)
    accused_name = models.CharField(max_length=100, blank=True, null=True)
    accused_address = models.TextField(blank=True, null=True)
    incident_date = models.DateTimeField()
    incident_location = models.TextField()
    description_of_incident = models.TextField()
    evidence = models.FileField(upload_to='fir_evidence/', blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('filed', 'Filed'),
            ('investigating', 'Investigating'),
            ('charge_sheeted', 'Charge Sheeted'),
            ('closed', 'Closed'),
        ],
        default='filed'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.fir_number)
    

class SheduleDuty(models.Model):
    info = models.TextField()
    date = models.DateField(auto_now_add=True)
    station = models.ForeignKey(police_station_registration, on_delete=models.SET_NULL, null=True)
    staff_info = models.ForeignKey(staff, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return(self.staff_info)
    

class Attendance(models.Model):
    att = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    staff = models.ForeignKey(staff, on_delete=models.SET_NULL, null=True)
    station = models.ForeignKey(police_station_registration, on_delete=models.SET_NULL, null=True)


class Salary(models.Model):
    DESIGNATION_CHOICE = [
        ('DGP', 'Director General of Police'),
        ('IGP', 'Inspector General of Police'),
        ('SP', 'Superintendent of Police'),
        ('DSP', 'Deputy Superintendent of Police'),
        ('CI', 'Circle Inspector'),
        ('SI', 'Sub Inspector'),
        ('ASI', 'Assistant Sub Inspector'),
        ('HC', 'Head Constable'),
        ('PC', 'Police Constable')
    ]
    designation = models.CharField(max_length=50, choices=DESIGNATION_CHOICE, unique=True)
    bs = models.IntegerField()
    da = models.IntegerField()
    hr = models.IntegerField()
    pf = models.IntegerField()
    total_salaty = models.IntegerField(null=True, blank=True)


class Complaint(models.Model):
    pet = models.ForeignKey(Petition, on_delete=models.CASCADE)
    user = models.ForeignKey(user_registration, on_delete=models.SET_NULL, null=True)
    msg = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.pet