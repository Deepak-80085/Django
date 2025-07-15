<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import LoginActivity

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        content = {
            'message': 'This is a protected view! You are authenticated.',
            'user': serializer.data
        }
        return Response(content)

def home_view(request):
    """Home page view."""
    return render(request, 'home.html')

@csrf_protect
def signup_view(request):
    """
    Signup view for new users.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        # Validate form inputs
        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'registration/signup.html')
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'registration/signup.html')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'registration/signup.html')
        
        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully! You can now log in.')
        return redirect('login')
    
    return render(request, 'registration/signup.html')

@csrf_protect
def login_view(request):
    """
    Login view that authenticates users and generates JWT tokens.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Record login activity
            LoginActivity.objects.create(
                user=user,
                ip_address=request.META.get('REMOTE_ADDR'),
                user_agent=request.META.get('HTTP_USER_AGENT', '')
            )
            
            messages.success(request, 'You have successfully logged in.')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'registration/login.html')

def logout_view(request):
    """Logout view."""
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')

@login_required
def profile_view(request):
    """User profile view displaying JWT tokens."""
    try:
        # Get tokens for the current user
        refresh = RefreshToken.for_user(request.user)
        
        # Get login history for current user
        login_history = LoginActivity.objects.filter(user=request.user).order_by('-login_datetime')[:5]
        
        context = {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'login_history': login_history
        }
        
        return render(request, 'profile.html', context)
    except Exception as e:
        messages.error(request, f"Error generating tokens: {str(e)}")
        return render(request, 'profile.html', {'error': str(e)})
=======
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .models import LoginActivity

class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        content = {
            'message': 'This is a protected view! You are authenticated.',
            'user': serializer.data
        }
        return Response(content)

def home_view(request):
    """Home page view."""
    return render(request, 'home.html')

@csrf_protect
def signup_view(request):
    """
    Signup view for new users.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        # Validate form inputs
        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'registration/signup.html')
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'registration/signup.html')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return render(request, 'registration/signup.html')
        
        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        messages.success(request, 'Account created successfully! You can now log in.')
        return redirect('login')
    
    return render(request, 'registration/signup.html')

@csrf_protect
def login_view(request):
    """
    Login view that authenticates users and generates JWT tokens.
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Record login activity
            LoginActivity.objects.create(
                user=user,
                ip_address=request.META.get('REMOTE_ADDR'),
                user_agent=request.META.get('HTTP_USER_AGENT', '')
            )
            
            messages.success(request, 'You have successfully logged in.')
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'registration/login.html')

def logout_view(request):
    """Logout view."""
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')

@login_required
def profile_view(request):
    """User profile view displaying JWT tokens."""
    try:
        # Get tokens for the current user
        refresh = RefreshToken.for_user(request.user)
        
        # Get login history for current user
        login_history = LoginActivity.objects.filter(user=request.user).order_by('-login_datetime')[:5]
        
        context = {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
            'login_history': login_history
        }
        
        return render(request, 'profile.html', context)
    except Exception as e:
        messages.error(request, f"Error generating tokens: {str(e)}")
        return render(request, 'profile.html', {'error': str(e)})
>>>>>>> 1d2a47fef390eff824b3bc7cf2ea9d7e421b8492
