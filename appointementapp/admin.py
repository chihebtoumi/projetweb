from django.contrib import admin

from .models import Appointement,Doctor

# Register your models here.
#admin.site.register(Appointement)
@admin.action(description="Confirmer les rendez-vous sélectionnés")
def confirm_appointement(modeladmin, request, queryset):
    queryset.update(status="CONFIRMED")
@admin.register(Appointement)
class AppointementAdminPers(admin.ModelAdmin):
    actions = [confirm_appointement]
    list_display = ("id", "reason", "status", "appointement_date", "doctor", "patient")
    list_filter = ("status", "appointement_date", "doctor", "patient")
    list_editable = ("status",)
    search_fields = ("reason", "doctor__username", "patient__username")
    list_per_page = 2 
    ordering = ("-appointement_date",)
    fieldsets = (
        ("Description", {
            'fields': ("reason", "status", "prescription")
        }),("Date + duration", {
            'fields': ("appointement_date", "duration_minutes")
        }),("Doctor + Patient", {
            'fields': ("patient","doctor")
        }) ,("planification", {
            'fields': ("created_at", "updated_at")

        })
        
    )
    readonly_fields = ("created_at", "updated_at")
