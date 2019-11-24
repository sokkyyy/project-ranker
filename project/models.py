from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/', default='avatar.png')
    bio = models.TextField(default='Add a bio')
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        default=1
    )
    # projects
    # contacts =
    @classmethod
    def get_user_profile(cls,user):
        profile = Profile.objects.get(user=user)
        return profile

    def __str__(self):
        return f'{self.bio}'     

class Project(models.Model):
    name = models.CharField(null=False,max_length=100)
    description = models.TextField(null=False)
    design = models.DecimalField(default=0.00,decimal_places=2,max_digits=20)
    usability = models.DecimalField(default=0.00,decimal_places=2,max_digits=20)
    content = models.DecimalField(default=0.00,decimal_places=2,max_digits=20)
    average = models.DecimalField(default=0.00,decimal_places=2,max_digits=20)
    project_pic = models.ImageField(upload_to='project_pics', null=False)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.name}'