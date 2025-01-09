from django.urls import path

from pelamar.controller.LamaranPageControl import ControllerLamaranPage
from pelamar.controller.ResumePageControl import ControllerResumePage
from pelamar.controller.NotificationPageControl import ControllerNotificationPage
from pelamar.controller.ReadNotificationPageControl import ControllerReadNotificationPage
from pelamar.controller.ReadLowonganPageControl import ControllerReadLowonganPage
from pelamar.controller.LowonganPageControl import ControllerLowonganPage

app_name = "pelamar"

urlpatterns = [
	path("myapply/",ControllerLamaranPage.as_view(),name="pelamar_apply"),
	path("resume/",ControllerResumePage.as_view(),name="pelamar_resume"),
	path("notif/",ControllerNotificationPage.as_view(),name="pelamar_notif"),
	path("read/<str:slug>",ControllerReadNotificationPage.as_view(),name="pelamar_read_notif"),
	path("apply/",ControllerLowonganPage.as_view(),name="pelamar_lowongan"),
	path("apply/<str:slug>",ControllerReadLowonganPage.as_view(),name="pelamar_read_lowongan"),

]