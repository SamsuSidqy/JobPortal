from django.urls import path

from administrator.controller.IndexPageControl import ControllerIndexPage
from administrator.controller.BuatPageControl import ControllerBuatPage
app_name = "admins"

urlpatterns = [
	path('',ControllerIndexPage.as_view(),name='admin_index'),
	path('makeapply/',ControllerBuatPage.as_view(),name='admin_create'),
]