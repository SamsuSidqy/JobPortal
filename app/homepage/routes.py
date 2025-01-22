from django.urls import path
from homepage.controller.HomePageControl import ControllerHomePage
from homepage.controller.ListLowonganPageControl import LowonganListControl
from homepage.controller.DetailLowonganPageControl import ControllerDetailPage
from homepage.controller.LoginPageControl import ControllerLoginPage
from homepage.controller.RegisterPageControl import ControllerRegisPage
from homepage.controller.ChangePasswordPage import ControllerChangePasswordPage
from homepage.controller.OtpPageControl import ControllerOTPPage
from homepage.controller.VerifyAnonymPageControl import ControllerVerifyAnonymPage
app_name = "home"

urlpatterns = [
	path('',ControllerHomePage.as_view(),name='halaman_utama'),
	path('lowongan/',LowonganListControl.as_view(),name='list_halaman'),
	path('detail/<str:slug>/',ControllerDetailPage.as_view(),name='detail_halaman'),
	path('login/',ControllerLoginPage.as_view(),name='login_halaman'),
	path("register/",ControllerRegisPage.as_view(),name='register_halaman'),
	path("change/password/",ControllerChangePasswordPage.as_view(),name='change_password_halaman'),
	path('verify/',ControllerOTPPage.as_view(),name='verify_otp'),
	path('account/verify/',ControllerVerifyAnonymPage.as_view(),name='verify_accounts'),
]