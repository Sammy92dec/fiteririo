from django.shortcuts import render
from django.views import generic
from .models import Session

class PostList(generic.ListView):
    model = Session