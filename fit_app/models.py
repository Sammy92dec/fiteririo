from django.db import models
from django.contrib.auth.models import User

TYPES = (
    ('pt', 'Pt'),
    ('cardio', 'Cardio'),
    ('strength', 'Strength'),
    ('stretch', 'Stretch'),
    ('core', 'Core'),
    )

class Session(models.Model):
    
    title = models.CharField(max_length=200)
    instructor_name = models.CharField(max_length=200)
    session_type = models.CharField(choices=TYPES,default='Pt')