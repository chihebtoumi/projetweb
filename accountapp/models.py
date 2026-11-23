from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator,MaxLengthValidator,RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError
# Create your models here.
class User(AbstractUser):
    pass
number_validator=RegexValidator(
        regex=r'^\d{8}$',
        message="le numero est incorrecte,ne respect le pattern"
    )

class Doctor(User):
    licence_number=models.CharField(max_length=6,unique=True,validators=[MinLengthValidator(6),MaxLengthValidator(6)])
    phone=models.CharField(max_length=8,validators=[number_validator])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    specialities=models.ManyToManyField(
        "accountapp.Speciality",
        related_name="doctors"
    )
    class Meta:
        verbose_name="Doctor"
        verbose_name_plural="Doctors"
def validate_birth_date(v):
    if(v>=timezone.localdate()):
        raise ValidationError("la date de naissance doit etre inferieur a la date d'aujourd'hui")
class Patient(User):
    national_id=models.CharField(max_length=8,unique=True ,validators=[number_validator])
    phone=models.CharField(max_length=8,validators=[number_validator])
    birth_date=models.DateField(validators=[validate_birth_date])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="Patient"
        verbose_name_plural="Patients"
        

class Speciality(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name="speciality"
        verbose_name_plural="specialities"
   
