from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import  Inquiry,User,UserCount

class BookInquiry(admin.ModelAdmin):
    list_display=('date','name','inquiry')

class BookUser(admin.ModelAdmin):
    list_display=('user','date')
admin.site.register(Inquiry,BookInquiry)
admin.site.register(User,BookUser)
admin.register(UserCount)(admin.ModelAdmin)