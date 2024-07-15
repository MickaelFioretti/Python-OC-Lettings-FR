from django.shortcuts import render


def index(request):
    """
    Vue pour la page d'accueil.

    Cette vue affiche la page d'accueil du site.

    Args:
        request (HttpRequest): L'objet de requête HTTP.

    Returns:
        HttpResponse: La réponse HTTP contenant le rendu de la page d'accueil.
    """
    return render(request, "index.html")
