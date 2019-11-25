from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
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
    name = models.CharField(max_length=100)
    description = models.TextField()
    design = models.IntegerField(default=0,validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ])
    usability = models.IntegerField(default=0,
    validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ])
    content = models.IntegerField(default=0,
    validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ])
    average = models.IntegerField(default=0,
    validators=[
        MinValueValidator(0),
        MaxValueValidator(10)
    ])
    project_pic = models.ImageField(upload_to='project_pic/')
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    @classmethod
    def get_user_projects(cls,profile):
        projects = cls.objects.filter(profile=profile)
        return projects

    def __str__(self):
        return f'{self.name}'