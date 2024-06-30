from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


COMPETENCE_TYPES = (
    ('beginner','Beginner'),
    ('intermediate','Intermediate'),
    ('advance','Advance'),
)

GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
    )


class Member(models.Model):
    """
    A member profile model for class history and
    maintaining sucess/fail story.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_alt = models.URLField(blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    competence_types = models.CharField(max_length=50, choices=COMPETENCE_TYPES,null=True, blank=True)


def __str__(self):
    return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()