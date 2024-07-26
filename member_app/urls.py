from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.Profile.as_view(), name='home'),
]