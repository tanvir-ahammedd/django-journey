from django.urls import path

from first_app.views import home, signup, loginuser, profile

urlpatterns = [
    path('', home),
    path('signup', signup, name='signup_page'),
    path('login', loginuser, name='login_page'),
    path('profile', profile, name='profile_page'),
]
