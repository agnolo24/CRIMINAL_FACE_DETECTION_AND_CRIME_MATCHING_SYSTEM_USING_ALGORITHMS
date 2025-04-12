from django.urls import path
from.import views

urlpatterns = [
    #public
    path('', views.guest_page, name='guest_page'),
    path('login_form/', views.login_check, name='login_form'),

    #police station
    path('police_station_reg_form/', views.police_station_reg_form, name='police_station_reg_form'),
    path('station_home/', views.station_home, name='station_home'),
    path('station_profile/', views.station_profile, name='station_profile'),
    path('edit_station_profile/', views.edit_station_profile, name='edit_station_profile'),
    path('view_enquiry/', views.view_enquiry, name='view_enquiry'),
    path('reply_to_public/<int:id>', views.reply_to_public, name='reply_to_public'),

    #user
    path('user_reg/', views.user_reg, name='user_reg'),
    path('user_home/', views.user_home, name='user_home'),
    path('user_profile/',views.user_profile,name='user_profile'),
    path('user_profile_edit/',views.user_profile_edit,name='user_profile_edit'),
    path('search_station/', views.search_station, name='search_station',),
    path('enquiry_function/<str:station_id>', views.enquiry_function, name='enquiry_function'),

    #staff
    path('staff_reg/', views.staff_reg_form, name='staff_reg'),
    path('staff_home/', views.staff_home, name='staff_home'),
    path('staff_profile/', views.staff_profile, name='staff_profile'),
    path('edit_staff_profile/', views.edit_staff_profile, name='edit_staff_profile'),

    #admin
    path('p_data_table/',views.police_station_details_table, name='p_data_table'),
    path('s_data_table/',views.staff_details_table, name='s_data_table'),
    path('accept_s/<str:station_id>', views.accept_s, name='accept_s'),
    path('reject_s/<str:station_id>', views.reject_s, name='reject_s'),
]
