from django.urls import path
from . import views

urlpatterns = [
    path("", views.profiles_index, name="profiles_index"),
    path("profiles/<str:username>/", views.profile, name="profile"),
]
