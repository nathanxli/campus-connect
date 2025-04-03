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
    all_others = UserProfile.objects.exclude(id=current_user.id).exclude(id__in=current_user.connections.all())

    # Score each user
    scored_users = []
    for user in all_others:
        score = calculate_match_score(current_user, user)
        scored_users.append((user, score))

    # Sort by descending score
    sorted_users = sorted(scored_users, key=lambda x: x[1], reverse=True)

    recommendations = [user for user, score in sorted_users]

    return render(request, 'network/network.html', {
        'current_user': current_user,
        'recommendations': recommendations,
        'connections': current_user.connections.all(),
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


### Functionality for Recommendation System
def calculate_match_score(user_a, user_b):
    def split_and_normalize(field):
        return set(item.strip().lower() for item in field.split(",") if item.strip())

    major_a = split_and_normalize(user_a.majors)
    major_b = split_and_normalize(user_b.majors)

    acad_a = split_and_normalize(user_a.academic_interests)
    acad_b = split_and_normalize(user_b.academic_interests)

    non_acad_a = split_and_normalize(user_a.non_academic_interests)
    non_acad_b = split_and_normalize(user_b.non_academic_interests)

    classes_a = split_and_normalize(user_a.current_classes)
    classes_b = split_and_normalize(user_b.current_classes)

    score = (
        len(major_a & major_b) * 3 +
        len(acad_a & acad_b) * 4 +
        len(classes_a & classes_b) * 3 +
        len(non_acad_a & non_acad_b) * 1
    )

    return score

