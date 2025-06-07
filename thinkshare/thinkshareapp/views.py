from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import Posts
from django.contrib import messages
from django.db import IntegrityError
# Create your views here.

def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('signin')
    return render(request, 'registration/login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')
        
        # Check if passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'registration/register.html')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
            return render(request, 'registration/register.html')
        
        # Check if email already exists (optional)
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered. Please use a different email.')
            return render(request, 'registration/register.html')
        
        try:
            # Create user
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Account created successfully!')
            login(request, user)
            return redirect('home')
        except IntegrityError:
            messages.error(request, 'An error occurred while creating your account. Please try again.')
            return render(request, 'registration/register.html')
    
    return render(request, 'registration/register.html')

@login_required
def home(request):
    posts = Posts.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

@login_required
def createpost(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('post-title')
        content = request.POST.get('post-content')
        photo = request.FILES.get('post-image')
        post = Posts(user=user, title=title, content=content, photo=photo)
        post.save()
        return redirect('home')
    return render(request, 'createpost.html')

@login_required
def editpost(request, post_id):
    post = Posts.objects.get(id=post_id)
    if request.method == 'POST':
        title = request.POST.get('post-title')
        content = request.POST.get('post-content')
        photo = request.FILES.get('post-image')
        post.title = title
        post.content = content
        post.photo = photo
        post.save()
        return redirect('home')
    return render(request, 'createpost.html', {'post': post})

@login_required
def deletepost(request, post_id):
    post = Posts.objects.get(id=post_id)
    post.delete()
    return redirect('home')

@login_required
def logout1(request):
    logout(request)
    return redirect('index')