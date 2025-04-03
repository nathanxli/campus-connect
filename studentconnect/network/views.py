from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile
from django.shortcuts import get_object_or_404

def get_current_user():
    print("testing")
    return UserProfile.objects.last() # Simulate a logged-in user
    

def profile_view_page(request):
    current_user = get_current_user()
    print("current user: ", current_user)
    return render(request, 'network/profile_view.html', {
        'profile': current_user
    })



def create_profile(request):
    print("accessing create profile page")
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


### Functionality for networks page
def network_page(request):
    current_user = get_current_user()

    # Simulated recommendations: all other users
    recommendations = UserProfile.objects.exclude(id=current_user.id).exclude(id__in=current_user.connections.all())
    
    connections = current_user.connections.all()

    return render(request, 'network/network.html', {
        'profile': current_user,
        'recommendations': recommendations,
        'connections': connections,
    })


def connect_user(request, user_id):
    current_user = get_current_user()
    target_user = get_object_or_404(UserProfile, id=user_id)

    # Prevent duplicate connection
    if target_user != current_user:
        current_user.connections.add(target_user)

    return redirect('network_page')

def disconnect_user(request, user_id):
    current_user = get_current_user()
    target_user = get_object_or_404(UserProfile, id=user_id)

    if target_user != current_user:
        current_user.connections.remove(target_user)

    return redirect('network_page')


