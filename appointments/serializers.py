from rest_framework import serializers

from .models import Doctor, Appointments, Patient


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

    def create(self, validated_data, *args, **kwargs):
        patient, created = Patient.objects.get_or_create(**validated_data.get('patient'))
        if created:
            kind = Appointments.NEW_APNTMNT
        else:
            kind = Appointments.FLW_UP_APTMNT
        validated_data['patient'] = patient
        validated_data['kind'] = kind
        return Appointments.objects.create(**validated_data)






