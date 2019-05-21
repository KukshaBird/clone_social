from django.shortcuts import render

# Create your views here.
# GROUPS viev.py
from django.contrib.auth.mixins import (LoginRequiredMixin,
										PermissionReqiredMixin)

from django.urls import reverse
from django.views import generic
from .models import Group,GroupMember

class CreateGroup(LoginRequiredMixin,generic.CreateView):
	fields = ('name', 'description')
	model = Group

class SingleGroup(generic.DetailView):
	model = Group

class ListGroups(generic.ListView):
	model = Group
	


