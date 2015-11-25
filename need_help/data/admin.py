from django.contrib import admin

from .models import Donor

class DonarAdmin(admin.ModelAdmin):

	admin.site.register(Donor)