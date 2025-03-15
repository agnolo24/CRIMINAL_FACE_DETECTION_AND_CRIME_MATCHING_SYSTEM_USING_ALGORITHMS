from django import forms
from . models import police_station_registration, login, staff


class police_station_registration_form(forms.ModelForm):
    class Meta:
        model = police_station_registration
        fields = ['station_id', 'address_line_1', 'address_line_2', 'district', 'city', 'contact']


class login_form(forms.ModelForm):
    class Meta:
        model = login
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'type': 'password'})
        }


class staff_registration_form(forms.ModelForm):
    class Meta:
        model = staff
        fields = ['staff_id', 'full_name', 'address', 'contact', 'designation', 'gender', 'date_of_birth']


class Login_check_form(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()
    