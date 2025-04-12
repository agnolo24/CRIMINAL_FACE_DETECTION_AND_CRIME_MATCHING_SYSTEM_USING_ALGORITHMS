from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from.models import police_station_registration, staff, user_registration, Enquiry, login as login_table

# Create your views here.


# starting of the guest model section

def guest_page(request):
    return render(request, 'guest/guest_page.html')

# This function is used for login(using this function login can be done by all three users station, staff, user(public))
def login_check(request):
    if request.method == 'POST':
        form = Login_check_form(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = get_object_or_404(login_table, email=email)
                if user.password == password:
                    if user.user_type == 'station':
                        if user.varification_status == 'varified':
                            request.session['station_id'] = user.id
                            return redirect('station_home')
                        else:
                            messages.error(request, 'Not Varified')
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
    return render(request, 'guest/login.html', {'login_form': form})


# ending of guest model views 

# starting of police model views

# This function is used for police_station_registration
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
            return redirect('guest_page')
    else:
        form = police_station_registration_form()
        log = login_form()
    return render(request, 'police_station/p_reg_form.html', {'p_reg_form': form, 'log': log})

def station_home(request):
    return render(request, 'police_station/station_home.html')

def station_profile(request):
    station_id = request.session.get('station_id')
    log_station = get_object_or_404(login_table, id = station_id)
    data = police_station_registration.objects.get(login_id = log_station)
    return render(request, 'police_station/station_profile.html', {'data' : data})

def edit_station_profile(request):
    station_id = request.session.get('station_id')
    log_station = get_object_or_404(login_table, id = station_id)
    data = police_station_registration.objects.get(login_id = log_station)
    if request.method == 'POST':
        form = edit_station_profile_form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('station_profile')
    else:
        form = edit_station_profile_form(instance=data)
    return render(request, 'police_station/edit_station_profile.html', {'form' : form})

def view_enquiry(request):
    login_id = request.session.get('station_id')
    station = police_station_registration.objects.get(login_id = login_id)
    station_id = station.station_id
    enquiry = Enquiry.objects.filter(station_id = station_id)
    return render(request, 'police_station/view_enquiry.html', {'enquirys':enquiry})

def reply_to_public(request, id):
    enquiry = get_object_or_404(Enquiry, id = id)
    if request.method == 'POST':
        form = Reply(request.POST)
        if form.is_valid():
            msg = form.cleaned_data['reply']
            enquiry.reply = msg
            enquiry.save()
            return redirect('view_enquiry')
    else:
        form = Reply()
    return render(request, 'police_station/reply.html', {'form' : form})

# ending of police model views

# starting of user(public) views

# This function is used for user(public) registration
def user_reg(request):
    if request.method == 'POST':
        form = user_registration_form(request.POST)
        log = login_form(request.POST)
        if form.is_valid() and log.is_valid():
            log_ins = log.save(commit=False)
            log_ins.user_type = 'user'
            log_ins.varification_status = 'varified'
            log_ins.save()
            form_ins = form.save(commit=False)
            form_ins.login_id = log_ins
            form_ins.save()
            return redirect('guest_page')
    else:
        form = user_registration_form()
        log = login_form()
    return render(request, 'public/user_registration_form.html', {'form' : form, 'log' : log})

def user_home(request):
    return render(request, 'public/user_home.html')

def user_profile(request):
    user_id=request.session.get('user_id')
    log_user=get_object_or_404(login_table,id=user_id)
    data=user_registration.objects.get(login_id=log_user)
    return render(request,'public/public_profile.html',{'data':data})

def user_profile_edit(request):
    user_id=request.session.get('user_id')
    log_user=get_object_or_404(login_table,id=user_id)
    data=user_registration.objects.get(login_id=log_user)
    if request.method=='POST':
        form=user_registration_form(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('user_profile')
    else:
        form=user_registration_form(instance=data)
    return render(request,'public/public_edit.html',{'form':form})

def search_station(request):
    if request.method == 'POST':
        form = search_station_form(request.POST)
        if form.is_valid():
            station_id = form.cleaned_data['Station_id']
            try:
                station = police_station_registration.objects.get(station_id = station_id)
                login_info = login_table.objects.get(id = station.login_id.id)
                if login_info.varification_status == 'varified':
                    return render(request, 'public/station_search_result.html', {'station' : station})
                else:
                    messages.error(request, 'police station is not varified')
            except police_station_registration.DoesNotExist:
                messages.error(request, 'Police station does not exist')
    else:
        form = search_station_form()
    return render(request, 'public/search_station.html', {'form' : form})

def enquiry_function(request, station_id):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            station = get_object_or_404(police_station_registration, station_id = station_id)
            obj.station_id = station
            user_login_id = request.session.get('user_id')
            user_id = get_object_or_404(user_registration, login_id = user_login_id)
            obj.user_id = user_id
            obj.save()
            return redirect('search_station')
    else:
        form = EnquiryForm()
    return render(request, 'public/enquiry.html', {'form':form})

# ending of user(public) model views

# starting of staff model views

# This function is used for staff_registration
def staff_reg_form(request):
    if request.method == 'POST':
        log = login_form(request.POST)
        form = staff_registration_form(request.POST)
        if form.is_valid() and log.is_valid():
            log_inst=log.save(commit=False)
            log_inst.user_type='staff'
            log_inst.varification_status = 'varified'
            log_inst.save()
            inst=form.save(commit=False)
            inst.login_id=log_inst
            inst.save()
            return redirect('login_form')
    else:
        form = staff_registration_form()
        log = login_form()
    return render(request, 'staff/s_reg_form.html', {'s_reg_form': form, 'log': log})

def staff_home(request):
    return render(request, 'staff/staff_home.html')

# To view the staff profile after the login
def staff_profile(request):
    staff_id = request.session.get('staff_id')
    log_staf = get_object_or_404(login_table, id = staff_id)
    data = staff.objects.get(login_id = log_staf)
    return render(request, 'staff/staff_profile.html', {'data' : data})

# To edit the staff data after login
def edit_staff_profile(request):
    staff_id = request.session.get('staff_id')
    log_staf = get_object_or_404(login_table, id = staff_id)
    data = staff.objects.get(login_id = log_staf)
    if request.method == 'POST':
        form = staff_edit_form(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('staff_profile')
    else:
        form = staff_edit_form(instance=data)
    return render(request, 'staff/edit_staff.html', {'form' : form})

# ending of staff model views

# starting of webadmin model views

# This is the function for showing the details of the police station we registred (used for admin)
def police_station_details_table(request):
    police_station_data = police_station_registration.objects.all()
    return render(request, 'web_admin/data.html',{'data1':police_station_data})

# This is the function for showing the details of the staff we registred (used for admin)
def staff_details_table(request):
    staff_data = staff.objects.all()
    return render(request, 'web_admin/data_staff.html',{'Datas':staff_data})

def accept_s(request, station_id):
    station = get_object_or_404(login, id = station_id)
    station.varification_status = 'varified'
    station.save()
    return redirect('p_data_table')

def reject_s(request, station_id):
    station = get_object_or_404(login, id = station_id)
    station.varification_status = 'reject'
    station.save()
    return redirect('p_data_table')

# ending of webadmin model view