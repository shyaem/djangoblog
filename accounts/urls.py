from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('profile/<str:fullname>/', views.profile_view, name="profile"),
    path('create_view/<str:fullname>/', views.create_view, name="profile1"),
    path('update_view/<str:fullname>/', views.update_view, name="profile2"),
    path('userprofile/<str:fullname>/', views.userprofile_view, name="profile3"),


]
