"""
models.py

Ce module contient les modèles pour l'application, incluant les définitions pour
`Address` et `Letting`.

- Address: Représente une adresse physique.
- Letting: Représente une location, associée à une adresse.
"""

from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator


class Address(models.Model):
    """
    Modèle représentant une adresse.

    Ce modèle stocke les détails d'une adresse, y compris le numéro de rue,
    le nom de la rue, la ville, l'état, le code postal et le code ISO du pays.

    Attributs :
    - number (PositiveIntegerField) : Numéro de la rue, valide jusqu'à 9999.
    - street (CharField) : Nom de la rue avec une longueur maximale de 64 caractères.
    - city (CharField) : Nom de la ville avec une longueur maximale de 64 caractères.
    - state (CharField) : État ou province avec une longueur fixe de 2 caractères.
    - zip_code (PositiveIntegerField) : Code postal avec une valeur maximale de 99999.
    - country_iso_code (CharField) : Code ISO du pays avec une longueur fixe de 3 caractères.

    Méthodes :
    - __str__() : Retourne une chaîne représentant l'adresse sous le format "numéro rue".

    Métadonnées :
    - db_table (str) : Nom de la table dans la base de données.
    Défini comme "oc_lettings_site_address".
    - verbose_name_plural (str) : Nom pluriel de l'objet utilisé dans
    l'interface d'administration. Défini comme "Addresses".
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
        Retourne une représentation en chaîne de caractères de l'adresse.

        Cette méthode renvoie une chaîne de caractères au format "numéro rue",
        ce qui permet de représenter
        l'adresse de manière lisible et concise. Cela facilite l'affichage de
        l'objet `Address` dans les
        interfaces utilisateur et les interfaces d'administration.

        Returns:
            str: Une chaîne représentant l'adresse sous le format "numéro rue".
        """
        return f"{self.number} {self.street}"

    class Meta:
        """
        Classe interne de configuration pour le modèle `Address`.

        Cette classe interne `Meta` est utilisée pour définir des options de
        métadonnées pour le modèle `Address`.
        Les options définies ici affectent le comportement et
        la représentation du modèle dans la base de données et
        dans l'interface d'administration Django.

        Attributs :
        - db_table (str) : Nom de la table dans la base de données qui
        sera utilisée pour stocker les instances du modèle.
          Dans ce cas, la table est nommée "oc_lettings_site_address".
        - verbose_name_plural (str) : Nom pluriel de l'objet utilisé dans
        l'interface d'administration Django. Défini comme "Addresses".
        """

        db_table = "oc_lettings_site_address"
        verbose_name_plural = "Addresses"


class Letting(models.Model):
    """
    Modèle représentant une annonce de location.

    Ce modèle stocke les informations d'une annonce de location,
    y compris le titre de l'annonce et l'adresse associée.

    Attributs :
    - title (CharField) : Titre de l'annonce avec une longueur maximale
    de 256 caractères.
    - address (OneToOneField) : Relation un-à-un avec le modèle `Address`.
    Cette relation assure qu'une annonce est associée à une seule adresse
    et vice versa.

    Méthodes :
    - __str__() : Retourne le titre de l'annonce comme représentation en chaîne
    de caractères de l'annonce.

    Métadonnées :
    - db_table (str) : Nom de la table dans la base de données.
    Défini comme "oc_lettings_site_letting".
    """

    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères du modèle `Letting`.

        Cette méthode renvoie le titre de l'annonce, ce qui permet
        une représentation lisible et identifiable de l'objet `Letting`
        lorsque celui-ci est affiché dans l'interface Django admin ou
        dans les requêtes qui affichent des objets `Letting`.

        Returns:
            str: Le titre de l'annonce.
        """
        return self.title

    class Meta:
        """
        Classe interne de configuration pour le modèle `Letting`.

        Cette classe interne `Meta` est utilisée pour définir
        des options de métadonnées pour le modèle `Letting`.
        Les options définies ici affectent le comportement
        et la représentation du modèle dans la base de données et
        dans l'interface d'administration Django.

        Attributs :
        - db_table (str) : Nom de la table dans la base de données
        qui sera utilisée pour stocker les instances du modèle.
          Dans ce cas, la table est nommée "oc_lettings_site_letting".
        """

        db_table = "oc_lettings_site_letting"
