from django.contrib import admin
from .models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    pass

admin.site.register(contact, ContactAdmin)