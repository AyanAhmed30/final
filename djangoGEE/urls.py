# djangoGEE/urls.py

from django.contrib import admin
from django.urls import path
from gee import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Root URL
    path('home/', views.home, name='home'),
    path('map/', views.map, name='map'),
    path('generate-ndvi-map/', views.generate_ndvi_map, name='generate_ndvi_map'),
    path('chart/', views.generate_chart, name='generate_chart'),
    path('gee/', views.GEE, name='gee'),
    path('result_options/', views.result_options, name='result_options'),
    path('result_options/temp_result/', views.temp_result, name='temp_results'),
    path('api/chart-data/', views.chart, name='chart_data_api'),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('settings/change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'), name='password_change'),
    path('settings/change_password/done', auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'), name='password_change_done'),
    path('account/', views.UserUpdateView.as_view(), name='my_account'),
]
