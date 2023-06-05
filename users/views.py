from django.shortcuts import render , redirect
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

from users.models import Profile
from .forms import CustomUserCreationForm , ProfileForm
from posts.models import Posts

def viewProfile(request , pk):
    profile = Profile.objects.get(id=pk)
    posts = profile.posts_set.all()

    context = {
        'profile':profile,
        'posts':posts
    }
    return render(request, 'users/profile.html',context)

@login_required(login_url='login')
def editProfile(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST , request.FILES , instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form':form
    }
    return render(request , 'users/editProfile.html',context)

def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request , user)
            return redirect('index')
    context = {
        'form':form,
    }
    return render(request , 'users/register.html',context)

def logInUser(request):
    
    if request.user.is_authenticated:
        return redirect('index')

    #  nqoftse metoda osht POST <HTML>
    if request.method == "POST":
        # i mormi emrin e inputeve nhtml dhe ja i lidhmi me variablat
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            # e kshyrmi se a osht usernemi ndatabaz
            user = User.objects.get(username=username)
        except:
            # nqoftse jo at'her e qojm ni message 
            """
            messages i regjistrojm tek main.html
            """
            messages.error(request , "Username does not exist")
        # nqoftese kejt jon nrregull at'her e bojm llog in 
        user = authenticate(request, username=username , password=password)
        # nqofte useri ndatabaz nuk osht i shprast , at'her e bojm llogin edhe e qojm tek profiles
        if user is not None:
            login(request , user)
            return redirect(request.GET['next'] if 'next' in request.GET else 'index')
        else:
        # nqoftse jo at'her e qesmi ket messazhin
            messages.error(request , "Username or password is incorrect")
        
    return render(request, 'users/login.html')

def UserLogOut(request):
    logout(request)
    return redirect('login')
