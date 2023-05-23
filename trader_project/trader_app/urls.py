from django.urls import path
from .view_functions.user import *
from .view_functions.auth import *
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:trader_id>/', user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('', home_to_create, name='home_to_create'),
    path('admin_dashboard/<int:trader_id>/', trader_details, name='trader_details'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]
