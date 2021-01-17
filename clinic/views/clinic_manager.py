from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth import get_user_model
from django.views.generic import DetailView

from ..models import Reserve, Clinic
from ..forms import ClinicSignUpForm
from ..decorators import clinic_required

User = get_user_model()


class ClinicSignUpView(CreateView):
    model = User
    form_class = ClinicSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'clinic_manager'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('clinic_manager:reservation_list')


@method_decorator([login_required, clinic_required], name='dispatch')
class ReservationListView(ListView):
    model = Reserve
    ordering = ('name',)
    context_object_name = 'reservations'
    template_name = 'clinic/clinic_manager/reservation_list.html'

    def get_queryset(self):
        clinic = self.request.user
        queryset = Reserve.objects.filter(clinic__user=clinic)
        return queryset


class Profile(DetailView):
    template_name = 'clinic/clinic_manager/profile.html'
    model = Clinic
    context_object_name = 'clinic_profile'

    def get_object(self):
        clinic = get_object_or_404(Clinic, pk=self.request.user.id)
        print(clinic.__dict__)
        return clinic
