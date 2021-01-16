"""CleanQ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from clinic.views import clinic,clinic_manager,patient
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('signup/', signup, name='signup'),
    path('', include('clinic.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', clinic.SignUpView.as_view(), name='signup'),
    path('accounts/signup/clinic-manager/', clinic_manager.ClinicSignUpView.as_view(), name='clinic_manager_signup'),
    path('accounts/signup/patient/', patient.PatientSignUpView.as_view(), name='patient_signup'),

]
