from django.contrib.auth import get_user_model 

from accounts.models import UserProfile

User = get_user_model()

def create_user(*args, **kwargs):
    new_user = User.objects.create_user(*args, **kwargs)
    UserProfile.objects.create(user=new_user)
    return new_user
