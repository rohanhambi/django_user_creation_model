from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Person
# Register your models here.


class PersonAdmin(admin.ModelAdmin):
    search_fields = ['User']


admin.site.register(User,UserAdmin)
admin.site.register(Person,PersonAdmin)
