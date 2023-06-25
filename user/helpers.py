from django.contrib.auth.models  import User
from .models import UsersProfile

def profile_finder(user):
    return UsersProfile.objects.get(pk=user.pk)