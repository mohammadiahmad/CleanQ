from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


def home(request):
    if request.user.is_authenticated:
        if request.user.is_clinic_manager:
            return redirect('clinic_manager:reservation_list')
        else:
            return redirect('clinic_manager:reservation_list')
    return render(request, 'clinic/home.html')
