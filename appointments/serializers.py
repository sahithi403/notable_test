from rest_framework import serializers
from rest_framework.exceptions import APIException

from .models import Doctor, Appointments, Patient
from libs.time_utils import time_slots

VALID_TIME_SLOTS = time_slots()


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Appointments
        fields = "__all__"

    def validate_appt_time(self, time):
        if time in VALID_TIME_SLOTS:
            return time
        else:
            raise serializers.ValidationError('Invalid Time Value')

    def create(self, validated_data, *args, **kwargs):
        doc_appts_count = Appointments.objects.filter(
            doctor=validated_data['doctor'],
            appt_date=validated_data['appt_date'],
            appt_time=validated_data['appt_time'],
        ).count()

        if doc_appts_count >= 3:
            raise APIException("Appointment time unavailable")

        patient, created = Patient.objects.get_or_create(**validated_data.get('patient'))
        if created:
            kind = Appointments.NEW_APNTMNT
        else:
            kind = Appointments.FLW_UP_APTMNT
        validated_data['patient'] = patient
        validated_data['kind'] = kind

        return Appointments.objects.create(**validated_data)






