from django.contrib import admin
from db import models


admin.site.register(models.Pengguna)
admin.site.register(models.Education)
admin.site.register(models.Lowongan)
admin.site.register(models.DisabeldForm)
admin.site.register(models.LocationLowongan)
admin.site.register(models.KategoriLowongan)
admin.site.register(models.ProfilePerusahaan)
admin.site.register(models.TipeLowongan)
admin.site.register(models.ApplyLowongan)
admin.site.register(models.Notification)
admin.site.register(models.AttachmentNotification)