from django.contrib import admin
from .models import *
from appointementapp.models import Appointement


# Register your models here.
admin.site.register(User)
class DoctorPerso(admin.StackedInline):
    model=Appointement
    extra=1
    fieldsets = (
        ("Description", {
            'fields': ("reason", "status", "prescription")
        }),("Date + duration", {
            'fields': ("appointement_date", "duration_minutes")
        }),("Patient", {
            'fields': ("patient",)

        })
        
    )
    readonly_fields = ("created_at", "updated_at")
class DoctorPersoClass(admin.ModelAdmin):
    inlines=[DoctorPerso,]
admin.site.register(Doctor,DoctorPersoClass)
admin.site.register(Patient)
admin.site.register(Speciality)
