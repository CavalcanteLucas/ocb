from django.contrib import admin

from .models import Culture

class CultureAdmin(admin.ModelAdmin):
    pass

admin.site.register(Culture, CultureAdmin)