from django.urls import path
from homepage.controller.HomePageControl import ControllerHomePage

app_name = "home"

urlpatterns = [
	path('',ControllerHomePage.as_view(),name='halaman_utama'),
]