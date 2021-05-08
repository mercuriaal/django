from django.contrib import admin
from .models import Phone, iPhone, Xiaomi, Samsung


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(iPhone)
class iPhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Samsung)
class SamsungAdmin(admin.ModelAdmin):
    pass


@admin.register(Xiaomi)
class XiaomiAdmin(admin.ModelAdmin):
    pass
