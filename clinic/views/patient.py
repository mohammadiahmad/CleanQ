from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView

from django.views.generic import DetailView
from ..models import Reserve, Patient

from ..forms import  PatientSignUpForm
from ..models import  User
from ..decorators import patient_required

class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('patient:reservation_list')

@method_decorator([login_required, patient_required()], name='dispatch')
class ReservationListView(ListView):
    model = Reserve
    ordering = ('name',)
    context_object_name = 'reservations'
    template_name = 'clinic/patient/reservation_list.html'

    def get_queryset(self):
        patient = self.request.user
        queryset = Reserve.objects.filter(clinic__user=patient)
        return queryset


@method_decorator([login_required, patient_required()], name='dispatch')
class Profile(DetailView):
    template_name = 'clinic/patient/profile.html'
    model = Patient
    context_object_name = 'patient_profile'

    def get_object(self):
        clinic = get_object_or_404(Patient, pk=self.request.user.id)
        print(clinic.__dict__)
        return clinic