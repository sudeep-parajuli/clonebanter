from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts import forms

# Create your views here.

class SignUp(CreateView):
    form_class = forms.userRegistrationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "register.html"
