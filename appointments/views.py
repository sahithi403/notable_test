from django.shortcuts import render
from rest_framework import mixins, status, viewsets
# Create your views here.

from .models import Appointments, Doctor
from .serializers import AppointmentSerializer, DoctorSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        return Doctor.objects.all()


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        return Appointments.objects.all()
