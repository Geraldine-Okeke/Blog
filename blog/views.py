# blog/views.py
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Post
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
  if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
          username = form.cleaned_data.get('username')
          password = form.cleaned_data.get('password')
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  return redirect('homepage')
  else:
      form = AuthenticationForm()
  return render(request, 'registration/login.html', {'form': form})

def homepage(request):
    posts = Post.objects.all()
    return render(request, 'blog/homepage.html', {'posts': posts})
  
def full_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    # Get the latest post added by the admin
    
    # Get the last 4 posts added by the admin
    latest_posts = Post.objects.filter(user=post.user).exclude(pk=post_id).order_by('-pub_date')[:4]

    context = {
        'post': post,
        'latest_posts': latest_posts,
    }

    return render(request, 'blog/full_post.html', context)