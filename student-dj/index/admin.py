from django.contrib import admin

from .models import Ticket
# from myproject.admin_site import custom_admin_site

@admin.register(Ticket)
class PersonAdmin(admin.ModelAdmin):
    pass