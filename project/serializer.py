from rest_framework import serializers
from .models import Profile,Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name','description','design','usability','content','average','project_pic','link','profile']


class ProfileSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True,read_only=True)

    class Meta:
        model = Profile
        fields = ['profile_pic','bio','projects']

