from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


COMPETENCE_TYPES = (
    ('beginner','Beginner'),
    ('intermediate','Intermediate'),
    ('advance','Advance'),
)


class Member(models.Model):
    """
    A member profile model for class history and
    maintaining sucess/fail story.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image_alt = models.URLField(blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    city = models.CharField(max_length=40, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    competence_types = models.CharField(max_length=50, choices=COMPETENCE_TYPES, default='beginner')

"""    
    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    
    Create or update the user profile

    if created:
        Member.objects.create(user=instance)

    instance.member.save()

class WishClass(models.Model):
    
    A model that keeps track of users classes join or PT sessions.
   
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type_class = models.ManyToManyField(Product, blank=True)
 """