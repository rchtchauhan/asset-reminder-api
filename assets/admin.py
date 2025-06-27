from django.contrib import admin

# Register your models here.
from .models import Asset, Notification, Violation

admin.site.register(Asset)
admin.site.register(Notification)
admin.site.register(Violation)