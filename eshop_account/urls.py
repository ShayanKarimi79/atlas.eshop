from django.urls import path
from .views import log_in,register,log_out,user_profile_page,edit_user_profile,profile_sidebar


urlpatterns = [
    path('login', log_in),
    path('register',register),
    path('logout',log_out),
    path('profile',user_profile_page),
    path('profile/edit',edit_user_profile)
]
