from django.urls import path
from.import views

urlpatterns = [
    #guest
    path('', views.guest_page, name='guest_page'),
    path('login_form/', views.login_check, name='login_form'),

    #police station
    path('police_station_reg_form/', views.police_station_reg_form, name='police_station_reg_form'),
    path('station_home/', views.station_home, name='station_home'),
    path('station_profile/', views.station_profile, name='station_profile'),
    path('edit_station_profile/', views.edit_station_profile, name='edit_station_profile'),
    path('view_enquiry/', views.view_enquiry, name='view_enquiry'),
    path('reply_to_public/<int:id>', views.reply_to_public, name='reply_to_public'),
    path('view_staff/', views.view_staff, name='view_staff'),
    path('accept_staff/<int:id>', views.accept_staff, name='accept_staff'),
    path('reject_staff/<int:id>', views.reject_staff, name='reject_staff'),
    path('view_petition/', views.view_petition, name='view_petition'),
    path('reply_to_petition/<int:id>', views.reply_to_petition, name='reply_to_petition'),
    path('criminal_registration/', views.criminal_registration, name='criminal_registration'),
    path('view_criminals/', views.view_criminals, name='view_criminals'),
    path('edit_criminal_data/<int:id>/', views.edit_criminal_data, name='edit_criminal_data'),
    path('delete_criminal_data/<int:id>', views.delete_criminal_data, name='delete_criminal_data'),
    path('fir_registration/<int:id>', views.fir_registration, name='fir_registration'),
    path('view_fir/', views.view_fir, name='view_fir'),
    path('update_fir/<int:id>', views.update_fir, name='update_fir'),
    path('shedule_duty/<str:staff_id>', views.shedule_duty, name='shedule_duty'),
    path('view_duty/<str:staff_id>/', views.view_duty, name='view_duty'),
    path('edit_duty/<int:id>', views.edit_duty, name='edit_duty'),
    path('delete_duty_info/<int:id>', views.delete_duty_info, name='delete_duty_info'),
    #user
    path('user_reg/', views.user_reg, name='user_reg'),
    path('user_home/', views.user_home, name='user_home'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('user_profile_edit/',views.user_profile_edit,name='user_profile_edit'),
    path('search_station/', views.search_station, name='search_station',),
    path('enquiry_function/<str:station_id>', views.enquiry_function, name='enquiry_function'),
    path('view_replay/', views.view_replay, name='view_replay'),
    path('petition/<str:id>', views.petition, name='petition'),
    path('view_petition_reply/', views.view_petition_reply, name='view_petition_reply'),
    path('view_most_wanted_criminals_public/', views.view_most_wanted_criminals_public, name='view_most_wanted_criminals_public'),
    path('view_fir_public/', views.view_fir_public, name='view_fir_public'),
    #staff
    path('staff_reg/', views.staff_reg_form, name='staff_reg'),
    path('staff_home/', views.staff_home, name='staff_home'),
    path('staff_profile/', views.staff_profile, name='staff_profile'),
    path('edit_staff_profile/', views.edit_staff_profile, name='edit_staff_profile'),
    path('view_most_wanted_criminals_staff/', views.view_most_wanted_criminals_staff, name='view_most_wanted_criminals_staff'),
    path('view_staff_duty/', views.view_staff_duty, name='view_staff_duty'),


    #admin
    path('admin_home/',views.admin_home, name='admin_home'),
    path('p_data_table/',views.police_station_details_table, name='p_data_table'),
    path('s_data_table/',views.staff_details_table, name='s_data_table'),
    path('accept_s/<str:station_id>', views.accept_s, name='accept_s'),
    path('reject_s/<str:station_id>', views.reject_s, name='reject_s'),
    

]
