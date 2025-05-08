from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('signup/', views.signup, name="signup_page"),
    path('login/', views.loginuser, name='login_page'),
    path('logout/', views.user_logout, name='logout_page'),
    path('profile/', views.profile, name='profile_page'),
    path('changepassword/', views.changePass, name='change_password'),
    path('changepassword2/', views.changePass2, name='change_password2'),
]
