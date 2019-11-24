from django.shortcuts import render,redirect
from .forms import RegForm
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':user.save()
        form = RegForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']            
            last_name = form.cleaned_data['last_name']

            user = User.objects.create_user(username,email,password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            
            profile = Profile(user=user)
            profile.save()
            return redirect(handle_login)

         
    form = RegForm()
    return render(request,'auth/registration.html',
    {"form":form})

def handle_login(request):
    return render(request,'auth/login.html')