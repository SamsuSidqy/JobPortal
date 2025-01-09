from django.urls import path
from homepage.controller.HomePageControl import ControllerHomePage
from homepage.controller.ListLowonganPageControl import LowonganListControl
from homepage.controller.DetailLowonganPageControl import ControllerDetailPage
from homepage.controller.LoginAndRegisterPageControl import ControllerLoginRegisPage
app_name = "home"

urlpatterns = [
	path('',ControllerHomePage.as_view(),name='halaman_utama'),
	path('lowongan/',LowonganListControl.as_view(),name='list_halaman'),
	path('detail/',ControllerDetailPage.as_view(),name='detail_halaman'),
	path('authentication/',ControllerLoginRegisPage.as_view(),name='login_halaman'),
]