from django.urls import path

from pelamar.controller.LamaranPageControl import ControllerLamaranPage
from pelamar.controller.ResumePageControl import ControllerResumePage
from pelamar.controller.LowonganPageControl import ControllerLowonganPage
from pelamar.controller.ReadLowonganPageControl import ControllerReadLowonganPage
from pelamar.controller.LogoutPageControl import LogoutUserController
from pelamar.controller.ReadFoto import ReadFotoController
from pelamar.controller.ReadCv import ReadCVController

app_name = "pelamar"

urlpatterns = [
	path("myapply/",ControllerLamaranPage.as_view(),name="pelamar_apply"),
	path("resume/",ControllerResumePage.as_view(),name="pelamar_resume"),
	path("apply/",ControllerLowonganPage.as_view(),name="pelamar_lowongan"),
	path("apply/<str:slug>/",ControllerReadLowonganPage.as_view(),name="pelamar_read_lowongan"),
	path("resume/photo/<str:file>",ReadFotoController.as_view(),name="photo_pelamar"),
	path("resume/cv/<str:file>",ReadCVController.as_view(),name='cv_pelamar'),
	path("logout/",LogoutUserController.as_view(),name="logout_pelamar"),
]