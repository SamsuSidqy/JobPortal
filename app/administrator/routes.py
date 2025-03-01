from django.urls import path

from administrator.controller.IndexPageControl import ControllerIndexPage
from administrator.controller.BuatPageControl import ControllerBuatPage
from administrator.controller.DataLowonganPageControl import ControllerDataLowonganPage
from administrator.controller.DataLamaranPageControl import ControllerDataLamaranPage
from administrator.controller.DataPelamarPageControl import ControllerDataPelamarPage
from administrator.controller.DataInterviewPageControl import ControllerDataInterviewPage
from administrator.controller.BuatKategoriPageControl import ControllerBuatKategoriPage
from administrator.controller.BuatLocationPageControl import ControllerBuatLocationPage
from administrator.controller.BuatEducationPageControl import ControllerBuatEducationPage
from administrator.controller.SettingsPageControl import ControllerSettingsPage
from administrator.controller.BuatTipePageControl import ControllerBuatTipePage
from administrator.controller.FileResponPageControl import ControllerReadCv, ControllerReadPhoto,ControllerReadFileCompany
from administrator.controller.LogoutPageControl import ControllerLogoutPage
app_name = "admins"

urlpatterns = [
	path('',ControllerIndexPage.as_view(),name='admin_index'),
	path('createlowongan/',ControllerBuatPage.as_view(),name='admin_create'),
	path('datalowongan/',ControllerDataLowonganPage.as_view(),name='admin_data_lowongan'),
	path('datalamaran/',ControllerDataLamaranPage.as_view(),name='admin_data_lamaran'),
	path('profile/<str:slug>/',ControllerDataPelamarPage.as_view(),name='admin_profile_pelamar'),
	path('iterview/',ControllerDataInterviewPage.as_view(),name='admin_data_interview'),
	path('kategori/',ControllerBuatKategoriPage.as_view(),name='admin_create_kategori'),
	path('location/',ControllerBuatLocationPage.as_view(),name='admin_create_location'),
	path('education/',ControllerBuatEducationPage.as_view(),name='admin_create_education'),
	path('tipelowongan/',ControllerBuatTipePage.as_view(),name='admin_create_tipe'),
	path('settings/',ControllerSettingsPage.as_view(),name='admin_settings'),
	path("cv/<str:file>",ControllerReadCv.as_view(),name="cv_pelamar"),
	path("photo/<str:file>",ControllerReadPhoto.as_view(),name='photo_pelamar'),
	path('file/<str:file>',ControllerReadFileCompany.as_view(),name='file_perusahaan'),
	path('logout/',ControllerLogoutPage.as_view(),name='logout_admin'),
]