<<<<<<< HEAD
from django.urls import path
from .views import (
    ProtectedView, 
    home_view, 
    login_view, 
    logout_view, 
    profile_view,
    signup_view
)

urlpatterns = [
    # API endpoints
    path('protected/', ProtectedView.as_view(), name='protected'),
    
    # Template-based views
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
=======
from django.urls import path
from .views import (
    ProtectedView, 
    home_view, 
    login_view, 
    logout_view, 
    profile_view,
    signup_view
)

urlpatterns = [
    # API endpoints
    path('protected/', ProtectedView.as_view(), name='protected'),
    
    # Template-based views
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('profile/', profile_view, name='profile'),
]
>>>>>>> 1d2a47fef390eff824b3bc7cf2ea9d7e421b8492
