from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Représente une adresse physique.

    Attributs:

        number (int): Le numéro de la rue, limité à 9999.
        street (str): Le nom de la rue, avec un maximum de 64 caractères.
        city (str): Le nom de la ville, avec un maximum de 64 caractères.
        state (str): L'état ou la région, exactement 2 caractères.
        zip_code (int): Le code postal, limité à 99999.
        country_iso_code (str): Le code ISO du pays, exactement 3 caractères.
    """

    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(
        max_length=3, validators=[MinLengthValidator(3)]
    )

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères de l'adresse.

        Returns:
            str: L'adresse formatée avec le numéro et le nom de la rue.
        """
        return f"{self.number} {self.street}"


class Letting(models.Model):
    """
    Représente une location avec un titre et une adresse associée.

    Attributs:

        title (str): Le titre de la location, avec un maximum de 256 caractères.
        address (Address): Une relation OneToOne avec le modèle Address.
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retourne une représentation sous forme de chaîne de caractères de la location.

        Returns:
            str: Le titre de la location.
        """
        return self.title
