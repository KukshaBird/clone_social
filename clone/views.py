# To use templates
from django.shortcuts import render
# reverse to needed urls when tap SignUp/Out
from django.urls import reverse_lazy
# Create view for SignUp form
from django.views.generic import CreateView

#Forms for SignUp and SignOut. In clone app folder.
from . import forms

# Create your views here.
class SignUp(CreateView):
	#connect to UserCreateForm
	form_class = forms.UserCreateForm
	success_url = reverse_lazy('login')
	template_name = 'clone/signup.html'
