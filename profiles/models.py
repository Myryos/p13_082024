"""
models.py
=========

Ce module contient les modèles pour l'application de gestion des profils.

Il définit les modèles suivants :
---------------------------------

- ``Profile`` : Représente un profil utilisateur, étendant ``User`` pour inclure des
  informations supplémentaires spécifiques à l'application.

Les modèles interagissent avec la base de données et sont associés aux tables via
les options de métadonnées.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle étendant ``User`` avec un champ pour la ville favorite de l'utilisateur.

    Attributs :
    - ``user`` (OneToOneField) : Relation un-à-un avec ``User``, supprimée avec
    l'utilisateur.
    - ``favorite_city`` (CharField) : Ville favorite, champ optionnel.

    Méthodes :
    - ``__str__()`` : Retourne le nom d'utilisateur comme représentation du profil.

    Métadonnées :
    - ``db_table`` (str) : Nom de la table de la base de données.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Retourne le nom d'utilisateur comme représentation du profil.
        """
        return self.user.username

    class Meta:
        """
        Métadonnées pour le modèle ``Profile``.

        Attributs :
        - ``db_table`` (str) : Nom de la table de la base de données.
        """
        db_table = "profiles_profile"
