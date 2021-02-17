from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import  Inquiry

class BookInquiry(admin.ModelAdmin):
    list_display=('date','name','inquiry')

admin.site.register(Inquiry,BookInquiry)