from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/', default='avatar.png')
    bio = models.TextField(default='Add a bio')
    # projects
    # contacts =
    
    def __str__(self):
        return f'{self.bio}'     

