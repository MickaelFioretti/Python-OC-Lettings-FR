from django.urls import path
from . import views

urlpatterns = [
    path("", views.lettings_index, name="lettings_index"),
    path("lettings/<int:letting_id>/", views.letting, name="letting"),
]
