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
                        if user.varification_status == 'varified':
                            request.session['staff_id'] = user.id
                            return redirect('staff_home')
                        else:
                            messages.error(request, 'Not Varified')
                    elif user.user_type == 'user':
                        request.session['user_id'] = user.id
                        return redirect('user_home')
                    elif user.user_type == 'admin':
                        request.session['admin_id'] = user.id
                        return redirect('admin_home')
                else:
                    messages.error(request, 'Invalid password')
            except login_form.DoesNotExist:
                messages.error(request, 'User does not exist')
    else:
        form = Login_check_form()
    return render(request, 'guest/login.html', {'login_form': form})


            # ending of guest model views 

            # starting of police station model views


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

def view_staff(request):
    station_login_id = request.session.get('station_id')
    login_ins = get_object_or_404(login_table, id = station_login_id)
    station_ins = get_object_or_404(police_station_registration, login_id = login_ins)
    staff_data = staff.objects.filter(station = station_ins)
    return render(request, 'police_station/view_staff.html', {'staff_data' : staff_data})

def accept_staff(request, id):
    login_data = get_object_or_404(login_table, id = id)
    login_data.varification_status = 'varified'
    login_data.save()
    return redirect('view_staff')

def reject_staff(request, id):
    login_data = get_object_or_404(login_table, id = id)
    login_data.varification_status = 'reject'
    login_data.save()
    return redirect('view_staff')

def view_petition(request):
    login_id = request.session.get('station_id')
    station = police_station_registration.objects.get(login_id = login_id)
    station_id = station.station_id
    petition = Petition.objects.filter(station_id = station_id)
    return render(request, 'police_station/view_petition.html', {'petition':petition})

def reply_to_petition(request, id):
    petition = get_object_or_404(Petition, id = id)
    if request.method == 'POST':
        form = Reply_petition(request.POST)
        if form.is_valid():
            reply = form.cleaned_data['reply']
            petition.reply = reply
            petition.save()
            return redirect('view_petition')
    else:
        form = Reply_petition()
    return render(request, 'police_station/reply_to_petition.html', {'form' : form})

def criminal_registration(request):
    if request.method == 'POST':
        form = CriminalRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            ins = form.save(commit=False)
            station_login_id = request.session.get('station_id')
            station_login_ins = get_object_or_404(login_table, id = station_login_id)
            station_reg_ins = get_object_or_404(police_station_registration, login_id = station_login_ins)
            ins.station = station_reg_ins
            ins.save()
            return redirect('station_home')
    else:
        form = CriminalRegistrationForm()
    return render(request, 'police_station/criminal_registration.html', {'form' : form})

def view_criminals(request):
    # station_login_id = request.session.get('station_id')
    # station_login_ins = get_object_or_404(login_table, id = station_login_id)
    # station_reg_ins = get_object_or_404(police_station_registration, login_id = station_login_ins)
    try:
        criminal_data = CriminalRegistration.objects.all()
        return render(request, 'police_station/view_criminals.html', {'criminal_data' : criminal_data})
    except CriminalRegistration.DoesNotExist:
        messages.error(request, 'No Criminal Registred')
        return redirect('police_station/station_home')
    
def edit_criminal_data(request, id):
    data = get_object_or_404(CriminalRegistration, id = id)
    if request.method == 'POST':
        form = CriminalRegistrationForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            form.save()
            return redirect('view_criminals')
    else:
        form = CriminalRegistrationForm(instance=data)
    return render(request, 'police_station/edit_criminal_data.html', {'form' : form})

def delete_criminal_data(request, id):
    data = get_object_or_404(CriminalRegistration, id = id)
    data.delete()
    return redirect('view_criminals')
    


            # ending of police station model views

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

def view_replay(request):
    login_id = request.session.get('user_id')
    login_info = get_object_or_404(login, id = login_id)
    reg_info = get_object_or_404(user_registration, login_id = login_info)
    enq = Enquiry.objects.filter(user_id = reg_info)
    return render(request, 'public/view_replay.html', {'enq':enq})

def petition(request, id):
    if request.method == 'POST':
        form = PetitionForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            user_id = request.session.get('user_id')
            user = get_object_or_404(login, id = user_id)
            user_data = get_object_or_404(user_registration, login_id = user)
            pet.user = user_data
            station = get_object_or_404(police_station_registration, station_id = id)
            pet.station = station
            pet.save()
            return redirect('search_station')
    else: 
        form = PetitionForm()
    return render(request, 'public/petition.html', {'form':form})

def view_petition_reply(request):
    login_id = request.session.get('user_id')
    login_info = get_object_or_404(login, id = login_id)
    reg_info = get_object_or_404(user_registration, login_id = login_info)
    pet = Petition.objects.filter(user_id = reg_info)
    return render(request, 'public/view_petition_reply.html', {'pet' : pet})

def view_most_wanted_criminals_public(request):
    try:
        criminal_data = CriminalRegistration.objects.all()
        return render(request, 'public/view_most_wanted_criminals_public.html', {'criminal_data' : criminal_data})
    except CriminalRegistration.DoesNotExist:
        messages.error(request, 'No Criminal Registred')
        return redirect('user_home')
    

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
            log_inst.varification_status = 'pending'
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

def view_most_wanted_criminals_staff(request):
    try:
        criminal_data = CriminalRegistration.objects.all()
        return render(request, 'staff/view_most_wanted_criminals_staff.html', {'criminal_data' : criminal_data})
    except CriminalRegistration.DoesNotExist:
        messages.error(request, 'No Criminal Registred')
        return redirect('staff_home')

            # ending of staff model views

            # starting of webadmin model views

def admin_home(request):
    return render(request, 'web_admin/admin_home.html')

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
