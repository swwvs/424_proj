from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import TVShow
from .forms import TVShowForm
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            # Add an error message if authentication fails
            messages.error(request, "Invalid username or password. Please try again.")
            return redirect('login')  # Redirect back to the login page if authentication fails

    return render(request, 'login.html')
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        if not username or not password:
            return render(request, 'register.html', {'error': 'Username and password are required.'})
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists.'})
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    shows = TVShow.objects.all()
    return render(request, 'home.html', {'shows': shows})


@login_required
def show_detail(request, show_id):
    show = get_object_or_404(TVShow, id=show_id)
    return render(request, 'show_detail.html', {'show': show})

@login_required
def add_show(request):
    if request.method == 'POST':
        form = TVShowForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TVShowForm()

    return render(request, 'add_show.html', {'form': form})


@login_required
def update_show(request, show_id):
    show = get_object_or_404(TVShow, id=show_id)
    
    if request.method == 'POST':
        form = TVShowForm(request.POST, request.FILES, instance=show)  # Handling file uploads
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TVShowForm(instance=show)
    
    return render(request, 'update_show.html', {'form': form})

@login_required
def delete_show(request, show_id):
    show = get_object_or_404(TVShow, id=show_id)
    if request.method == 'POST':
        show.delete()
        return redirect('home')  # Redirect to the list of TV shows after deletion
    return render(request, 'delete_show.html', {'show': show})  # Optional confirmation page
