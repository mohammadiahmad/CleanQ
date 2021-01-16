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
from ..models import Reserve
from ..forms import  ClinicSignUpForm

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
        return redirect('clinic_manager:reserverion_list')


class ReservationListView(ListView):
    model = Reserve
    ordering = ('name', )
    context_object_name = 'quizzes'
    template_name = 'clinic/clinic_manager/reservation_list.html.html'

    def get_queryset(self):
        clinic = self.request.user
        queryset = Reserve.objects.filter(clinic__user=clinic)
        return queryset