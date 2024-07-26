from django.shortcuts import render
from django.shortcuts import render
from django.views import generic
from .models import Member

class Profile(generic.ListView):
    queryset = Member.objects.all()
    template_name = "profile.html"