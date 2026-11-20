from django.db import models
from accountapp.models import Doctor
# Create your models here.
class Appointement(models.Model):
    reason=models.TextField()
    prescription=models.FileField(
        blank=True,
        upload_to='prescriptions/'
    )
    class Status(models.TextChoices):
        PENDING="PENDING","en attente"
        CONFIRMED="CONFIRMED","confirme"
        CANCELLED="CANCELLED","annule"
    status=models.CharField(max_length=10,choices=Status.choices,default=Status.PENDING)
    duration_minutes=models.PositiveIntegerField(default=30)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    appointement_date=models.DateTimeField()
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name="appointements")
    patient=models.ForeignKey("accountapp.Patient",on_delete=models.CASCADE,related_name="appointements")
    class Meta:
        oredering=["appointement_date"]
        constraints=[
            models.UniqueConstraint(
                fields=["doctor","appointement_date"],
                name="unicite_patient-doctor-date",
                violation_error_message="ce docteur possede un rdv avec cette date"
            )
        ]