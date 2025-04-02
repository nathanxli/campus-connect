from django.shortcuts import render
from .forms import UserProfileForm

def get_current_user():
    from .models import UserProfile
    return UserProfile.objects.first()

# Create your views here.
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