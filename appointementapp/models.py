from django.db import models
from accountapp.models import Doctor
from django.utils import timezone
from django.core.exceptions import ValidationError
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
    def clean(self):
        modified_date=self._state.adding or (
            Appointement.objects.filter(pk=self.pk,appointement_date=self.appointement_date).exists()
            )
        if modified_date and self.appointement_date<=timezone.now():
            raise ValidationError("la date du rendez-vous doit etre superieur a la date de creation")
    class Meta:
        ordering=["appointement_date"]
        constraints=[
            models.UniqueConstraint(
                fields=["doctor","appointement_date"],
                name="unicite_patient-doctor-date",
                violation_error_message="ce docteur possede un rdv avec cette date"
            )
        ]
    def __str__(self):
        return f"Rendez-vous du {self.appointement_date} avec le docteur {self.doctor.username} pour le patient {self.patient.username}"