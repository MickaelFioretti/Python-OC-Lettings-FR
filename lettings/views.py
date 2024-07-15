from django.shortcuts import render
from .models import Letting


def lettings_index(request):
    """
    Vue pour l'index des locations.

    Cette vue affiche une liste de toutes les locations disponibles.

    Args:
        request (HttpRequest): L'objet de requête HTTP.

    Returns:
        HttpResponse: La réponse HTTP contenant le rendu de la page des locations.
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings_index.html", context)


def letting(request, letting_id):
    """
    Vue pour une location spécifique.

    Cette vue affiche les détails d'une location basée sur l'ID de la location fourni.

    Args:
        request (HttpRequest): L'objet de requête HTTP.
        letting_id (int): L'ID de la location à afficher.

    Returns:
        HttpResponse: La réponse HTTP contenant le rendu de la page de la location.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "letting.html", context)
