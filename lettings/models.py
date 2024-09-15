"""
models.py

Ce module contient les modèles pour l'application, incluant les définitions pour
`Address` et `Letting`.

- `Address` : Représente une adresse physique.
- `Letting` : Représente une location, associée à une adresse.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse physique.

    Stocke les détails d'une adresse, y compris le numéro de rue, le nom de la rue,
    la ville, l'état, le code postal, et le code ISO du pays.

    Attributs :
    - `number` (PositiveIntegerField) : Numéro de rue, valide jusqu'à 9999.
    - `street` (CharField) : Nom de la rue, longueur maximale de 64 caractères.
    - `city` (CharField) : Nom de la ville, longueur maximale de 64 caractères.
    - `state` (CharField) : État ou province, longueur fixe de 2 caractères.
    - `zip_code` (PositiveIntegerField) : Code postal, valeur maximale de 99999.
    - `country_iso_code` (CharField) : Code ISO du pays, longueur fixe de 3 caractères.

    Méthodes :
    - `__str__()` : Retourne une chaîne représentant l'adresse sous le format
    "numéro rue".

    Métadonnées :
    - `db_table` (str) : Nom de la table dans la base de données, "lettings_address".
    - `verbose_name_plural` (str) : Nom pluriel de l'objet dans l'admin, "Addresses".
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
        Retourne une chaîne de caractères de l'adresse.

        La chaîne est au format "numéro rue", représentant l'adresse de manière
        lisible et concise.

        Returns:
            str: Chaîne représentant l'adresse au format "numéro rue".
        """
        return f"{self.number} {self.street}"

    class Meta:
        """
        Configuration interne pour le modèle `Address`.

        Définit les options de métadonnées pour le modèle `Address`.

        Attributs :
        - `db_table` (str) : Nom de la table dans la base de données, "lettings_address".
        - `verbose_name_plural` (str) : Nom pluriel dans l'admin, "Addresses".
        """

        db_table = "lettings_address"
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Modèle représentant une annonce de location.

    Stocke les informations d'une annonce de location, incluant le titre et
    l'adresse associée.

    Attributs :
    - `title` (CharField) : Titre de l'annonce, longueur maximale de 256 caractères.
    - `address` (OneToOneField) : Relation un-à-un avec le modèle `Address`.

    Méthodes :
    - `__str__()` : Retourne le titre de l'annonce comme chaîne de caractères.

    Métadonnées :
    - `db_table` (str) : Nom de la table dans la base de données, "lettings_letting".
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retourne une chaîne de caractères du titre de l'annonce.

        La chaîne représente le titre de l'annonce, ce qui est utile dans
        les interfaces d'administration et autres contextes.

        Returns:
            str: Titre de l'annonce.
        """
        return self.title

    class Meta:
        """
        Configuration interne pour le modèle `Letting`.

        Définit les options de métadonnées pour le modèle `Letting`.

        Attributs :
        - `db_table` (str) : Nom de la table dans la base de données, "lettings_letting".
        """

        db_table = "lettings_letting"
