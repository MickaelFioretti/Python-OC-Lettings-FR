from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Représente le profil utilisateur associé à un compte utilisateur.

    Attributs:
        user (User): Une relation OneToOne avec le modèle User de Django.

        favorite_city (str): La ville préférée de l'utilisateur, peut être laissée vide.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères du profil.

        Returns:
            str: Le nom d'utilisateur associé à ce profil.
        """
        return self.user.username
