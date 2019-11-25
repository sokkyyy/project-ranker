from django.shortcuts import render,redirect
from .forms import RegForm,LoginForm,ProjectForm
from django.contrib.auth.models import User
from .models import Profile,Project
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request,'home.html',{"projects":projects})

def register(request):
    if request.method == 'POST':
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
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(request,user)
                return redirect(home)
            else:
                # HANDLE INVALID LOGIN
                print('None')

    form = LoginForm()
    return render(request,'auth/login.html',{"form":LoginForm})

def handle_logout(request):
    logout(request)
    return redirect(handle_login)

def user_profile(request):
    user = request.user
    profile = Profile.get_user_profile(user)

    form = ProjectForm()
    projects = Project.get_user_projects(profile)


    return render(request,'profile.html',{"profile":profile,"form":form,"projects":projects})

def handle_project_upload(request):
    profile = Profile.get_user_profile(request.user)
    print(profile)



    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        pic = request.FILES['project_pic']
        project = Project(name=name,description=description,project_pic=pic,profile=profile)
        project.save()
        

    return redirect(user_profile)

def project_details(request,project_id):
    project = Project.objects.get(pk=project_id)
    return render(request,'project-details.html',
    {"project":project})