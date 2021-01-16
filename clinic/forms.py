from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Patient,Clinic
from django.db import transaction
from django.contrib.auth import get_user_model
User = get_user_model()

class ClinicSignUpForm(UserCreationForm):
    clinic_name = forms.CharField(help_text='Required.')
    address = forms.CharField(help_text='Required.')
    phone_number = forms.CharField(help_text='Required.')

    class Meta:
        model = User
        fields = ('clinic_name', 'username', 'password1', 'password2', 'address', 'phone_number')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_clinic_manager = True
        user.save()
        clinic = Clinic.objects.create(user=user)
        clinic.clinic_name = self.cleaned_data.get('clinic_name')
        clinic.phone_number = self.cleaned_data.get('phone_number')
        clinic.address = self.cleaned_data.get('address')
        clinic.save()

        return user

class PatientSignUpForm(UserCreationForm):
    phone_number = forms.CharField(help_text='Required.')
    address = forms.CharField(help_text='Required.')
    gender = forms.CharField(help_text='Required.')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2', 'address', 'phone_number', 'gender')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.gender=self.cleaned_data.get('gender')
        patient.phone_number=self.cleaned_data.get('phone_number')
        patient.address=self.cleaned_data.get('address')
        patient.save()

        return user


