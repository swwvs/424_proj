from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import TVShow
from .forms import TVShowForm
from django.contrib import messages
import datetime


# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have logged in successfully!')
            return redirect('home')  # Redirect to the home page or dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')


# Register view
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        # Basic validation checks
        if password != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'register.html')
        
        # Create the new user
        user = User.objects.create_user(username=username, password=password)
        messages.success(request, 'You have registered successfully!')
        return redirect('login')  # Redirect to the login page after successful registration
    
    return render(request, 'register.html')



# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')


@login_required
def home(request):
    shows = TVShow.objects.all()
    return render(request, 'home.html', {'shows': shows})


@login_required
def show_detail(request, show_id):
    show = get_object_or_404(TVShow, id=show_id)
    return render(request, 'show_detail.html', {'show': show})

# Add show view

@login_required
def add_show(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        release_date = request.POST.get('release_date')
        rating = request.POST.get('rating')
        seasons = request.POST.get('seasons')
        episodes_per_season = request.POST.get('episodes_per_season')
        photo = request.FILES.get('photo')

        if not release_date:
            messages.error(request, "Release date is required!")

        else:
            # Continue with saving the TV show
            TVShow.objects.create(
                title=title,
                genre=genre,
                description=description,
                release_date=release_date,
                rating=rating,
                seasons=seasons,
                episodes_per_season=episodes_per_season,
                photo=photo
            )
            messages.success(request, 'TV Show added successfully!')
            return redirect('home')

    return render(request, 'add_show.html')



# Update show view
@login_required
def update_show(request, show_id):
    # Fetch the TV show object you want to update
    show = TVShow.objects.get(id=show_id)

    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        description = request.POST.get('description')
        release_date = request.POST.get('release_date')
        rating = request.POST.get('rating')
        seasons = request.POST.get('seasons')
        episodes_per_season = request.POST.get('episodes_per_season')
        photo = request.FILES.get('photo')

        # Validation for missing release date
        if not release_date:
            messages.error(request, "Release date is required!")
        else:
            # Update the TV show with the new data
            show.title = title
            show.genre = genre
            show.description = description
            show.release_date = release_date
            show.rating = rating
            show.seasons = seasons
            show.episodes_per_season = episodes_per_season
            if photo:
                show.photo = photo
            show.save()
            messages.success(request, 'TV Show updated successfully!')
            return redirect('home')

    return render(request, 'update_show.html', {'show': show})

@login_required
def delete_show(request, show_id):
    show = get_object_or_404(TVShow, id=show_id)
    if request.method == 'POST':
        show.delete()
        messages.success(request, f'The show "{show.title}" has been deleted successfully!')
        return redirect('home')
    return render(request, 'delete_show.html', {'show': show})
