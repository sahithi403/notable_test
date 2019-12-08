from django.db import models


# Create your models here.
class Appointments(models.Model):
    NEW_APNTMNT = 'NEW'
    FLW_UP_APTMNT = 'FLW'
    DEFAULT_APT_CHC = NEW_APNTMNT
    APPOINTMENT_CHOICES = [
        (NEW_APNTMNT, 'New'),
        (FLW_UP_APTMNT, 'Follow-Up')
    ]

    doctor = models. ForeignKey("Doctor", on_delete=models.CASCADE)
    patient = models.ForeignKey("Patient", on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    kind = models.CharField(max_length=3, choices=APPOINTMENT_CHOICES, default=DEFAULT_APT_CHC)

    @property
    def patient_first_name(self):
        return self.patient.first_name

    @property
    def patient_last_name(self):
        return self.patient.last_name


class NotableUser(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.first_name} {self.last_name} : {self.id}"


class Doctor(NotableUser):
    email = models.CharField(max_length=256)


class Patient(NotableUser):
    pass
