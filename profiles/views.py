from django.shortcuts import render
from .models import Profile


# Create your views here.
def profiles_index(request):
    """
    Vue pour l'index des profils.

    Cette vue affiche une liste de tous les profils utilisateurs disponibles.

    Args:
        request (HttpRequest): L'objet de requête HTTP.

    Returns:
        HttpResponse: La réponse HTTP contenant le rendu de la page des profils.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles_index.html", context)


def profile(request, username):
    """
    Vue pour un profil utilisateur spécifique.

    Cette vue affiche les détails d'un profil utilisateur basé sur le nom d'utilisateur fourni.

    Args:
        request (HttpRequest): L'objet de requête HTTP.
        username (str): Le nom d'utilisateur du profil à afficher.

    Returns:
        HttpResponse: La réponse HTTP contenant le rendu de la page du profil.
    """
    profile = Profile.objects.get(user__username=username)
    context = {"profile": profile}
    return render(request, "profile.html", context)
