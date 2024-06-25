from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def member_page(request):
    return HttpResponse("Hello member")