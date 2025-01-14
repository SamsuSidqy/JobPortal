from django.urls import path
from homepage.controller.HomePageControl import ControllerHomePage
from homepage.controller.ListLowonganPageControl import LowonganListControl
from homepage.controller.DetailLowonganPageControl import ControllerDetailPage
from homepage.controller.LoginPageControl import ControllerLoginPage
from homepage.controller.RegisterPageControl import ControllerRegisPage
app_name = "home"

urlpatterns = [
	path('',ControllerHomePage.as_view(),name='halaman_utama'),
	path('lowongan/',LowonganListControl.as_view(),name='list_halaman'),
	path('detail/<str:slug>/',ControllerDetailPage.as_view(),name='detail_halaman'),
	path('login/',ControllerLoginPage.as_view(),name='login_halaman'),
	path("register/",ControllerRegisPage.as_view(),name='register_halaman'),
]