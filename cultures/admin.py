from django.contrib import admin

from .models import Culture


@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    list_display = [
        'genetic_name',
        'origin',
        'start_date',
        'flowering_date',
        'harvest_date',
        'harvest_weight',
        'drying_date',
        'drying_weight',
        'storage_date',
        'discarded',
        'discard_reason',
    ]
    list_filter = [
        'genetic_name',
        'origin',
        'discarded',
        'discard_reason',
    ]
    search_fields = [
        'genetic_name',
    ]
    ordering = [
        'start_date',
    ]