from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import police_station_registration_form, login_form, staff_registration_form, Login_check_form, user_registration_form
from.models import police_station_registration, staff, login as login_table

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def admin(request):
    return render(request, 'admin.html')


# this function is used for police_station_registration
def police_station_reg_form(request):
    if request.method == 'POST':
        log = login_form(request.POST)
        form = police_station_registration_form(request.POST)
        if form.is_valid() and log.is_valid():
            log_inst=log.save(commit=False)
            log_inst.user_type='station'
            log_inst.save()
            inst=form.save(commit=False)
            inst.login_id=log_inst
            inst.save()
            return redirect('index')
    else:
        form = police_station_registration_form()
        log = login_form()
    return render(request, 'p_reg_form.html', {'p_reg_form': form, 'log': log})


# this function is used for staff_registration
def staff_reg_form(request):
    if request.method == 'POST':
        log = login_form(request.POST)
        form = staff_registration_form(request.POST)
        if form.is_valid() and log.is_valid():
            log_inst=log.save(commit=False)
            log_inst.user_type='staff'
            log_inst.save()
            inst=form.save(commit=False)
            inst.login_id=log_inst
            inst.save()
            return redirect('index')
    else:
        form = staff_registration_form()
        log = login_form()
    return render(request, 's_reg_form.html', {'s_reg_form': form, 'log': log})


def user_reg(request):
    if request.method == 'POST':
        form = user_registration_form(request.POST)
        log = login_form(request.POST)
        if form.is_valid() and log.is_valid():
            log_ins = log.save(commit=False)
            log_ins.user_type = 'user'
            log_ins.save()
            form_ins = form.save(commit=False)
            form_ins.login_id = log_ins
            form_ins.save()
            return redirect('index')
    else:
        form = user_registration_form()
        log = login_form()
    return render(request, 'user_registration_form.html', {'form' : form, 'log' : log})

# this function is used for login
def login_check(request):
    if request.method == 'POST':
        form = Login_check_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email, password)
            try:
                user = get_object_or_404(login_table, email=email)
                if user.password == password:
                    if user.user_type == 'station':
                        request.session['station_id'] = user.id
                        return redirect('station_home')
                    elif user.user_type == 'staff':
                        request.session['staff_id'] = user.id
                        return redirect('staff_home')
                    elif user.user_type == 'user':
                        request.session['user_id'] = user.id
                        return redirect('user_home')
                else:
                    messages.error(request, 'Invalid password')
            except login_form.DoesNotExist:
                messages.error(request, 'User does not exist')
    else:
        form = Login_check_form()
    return render(request, 'login.html', {'login_form': form})
    


#this is the function for showing the details of the police station we registred
def police_station_details_table(request):
    police_station_data = police_station_registration.objects.all()
    return render(request, 'data.html',{'Datas':police_station_data})

def staff_details_table(request):
    staff_data = staff.objects.all()
    return render(request, 'data_staff.html',{'Datas':staff_data})

def staff_home(request):
    return render(request, 'staff_home.html')

def station_home(request):
    return render(request, 'station_home.html')

def user_home(request):
    return render(request, 'user_home.html')

