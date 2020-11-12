from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import RegistrationForm


class SignUpView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/sign_up.html'
    success_url = reverse_lazy('accounts:login')
