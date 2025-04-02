from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile

def get_current_user():
    from .models import UserProfile
    return UserProfile.objects.first() # Simulate a logged-in user


def network_page(request):
    current_user = get_current_user()

    # Simulated recommendations: all other users
    recommendations = UserProfile.objects.exclude(id=current_user.id)
    
    # Connections: for now, just hardcode none or fake some later
    connections = []  # Can simulate with a list of UserProfile objects

    return render(request, 'network/network.html', {
        'current_user': current_user,
        'recommendations': recommendations,
        'connections': connections,
    })



def create_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_created')  # Placeholder success page
    else:
        form = UserProfileForm()
    return render(request, 'network/create_profile.html', {'form': form})

def home(request):
    return render(request, 'network/home.html')

def network_page(request):
    return render(request, 'network/network.html')

def profile_view_page(request):
    return render(request, 'network/profile_view.html')