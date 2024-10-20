from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


def homepage(request):
    return render(request, 'homepage.html')  

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('homepage.html')  # Redirect to homepage after successful login
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'login.html')
    
    return render(request, 'login.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate password confirmation
        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'signup.html')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'signup.html')

        # Create a new user
        User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, "Registration successful! You can now log in.")
        return redirect('login')  # Adjust this based on your URL name for login

    return render(request, 'signup.html')
