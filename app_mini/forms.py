from django import forms
from . models import *


class login_form(forms.ModelForm):
    class Meta:
        model = login
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(attrs={'type': 'password'})
        }


class Login_check_form(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()


class police_station_registration_form(forms.ModelForm):
    class Meta:
        model = police_station_registration
        fields = ['station_id', 'address_line_1', 'address_line_2', 'district', 'city', 'contact']


class edit_station_profile_form(forms.ModelForm):
    class Meta:
        model = police_station_registration
        fields = ['address_line_1', 'address_line_2', 'district', 'city', 'contact']


class Reply(forms.Form):
    reply = forms.CharField(widget=forms.Textarea)


class user_registration_form(forms.ModelForm):
    class Meta:
        model = user_registration
        fields = ['fullname', 'contact']
        widgets = {
            'fullname' : forms.TextInput(attrs={'class' : 'form-control'}),
            'contact' : forms.TextInput(attrs={'class' : 'form-control'})
        }


class search_station_form(forms.Form):
    Station_id = forms.CharField()


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['enquiry_data']


class staff_registration_form(forms.ModelForm):
    class Meta:
        model = staff
        fields = ['staff_id', 'full_name', 'address', 'contact', 'designation', 'gender', 'date_of_birth', 'station']
        widgets = {'staff_id' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'full_name' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'address' : forms.Textarea(attrs={'class' : 'form-control'}),
                   'contact' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'designation' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'gender' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'date_of_birth' : forms.DateInput(attrs={'class' : 'form-control', 'type': 'date'})
        }


class staff_edit_form(forms.ModelForm):
    class Meta:
        model = staff
        fields = ['full_name', 'address', 'contact', 'designation', 'gender', 'date_of_birth']
        widgets = {
                   'full_name' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'address' : forms.Textarea(attrs={'class' : 'form-control'}),
                   'contact' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'designation' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'gender' : forms.TextInput(attrs={'class' : 'form-control'}),
                   'date_of_birth' : forms.DateInput(attrs={'class' : 'form-control', 'type': 'date'})
                   }

class PetitionForm(forms.ModelForm):
    class Meta:
        model = Petition
        fields = ['petition_text']
    

class Reply_petition(forms.Form):
    reply = forms.CharField(widget=forms.Textarea)


class CriminalRegistrationForm(forms.ModelForm):
    class Meta:
        model = CriminalRegistration
        fields = ['full_name', 'dob', 'case', 'height', 'weight', 'gender', 'photo']


