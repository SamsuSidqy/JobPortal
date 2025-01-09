
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('homepage.routes',namespace='home')),
    path('administrator/',include('administrator.routes',namespace='admins')),
    path("users/",include("pelamar.routes",namespace="pelamar")),
]
