from django.urls import path
from.import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login/',views.login, name='login'),
    path('loc_admin/', views.admin, name='loc_admin'),
    path('p_station_reg/', views.police_station_reg_form, name='p_station_reg'),
    path('staff_reg/', views.staff_reg_form, name='staff_reg'),
    path('login_form/', views.login_check, name='login_form'),
    path('p_data_table/',views.police_station_details_table, name='p_data_table'),
    path('s_data_table/',views.staff_details_table, name='s_data_table'),
    path('staff_home/', views.staff_home, name='staff_home'),
]
