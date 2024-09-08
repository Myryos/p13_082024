"""
models.py

Ce module contient les modèles de données pour l'application de gestion des
profils.

Il définit les modèles suivants :
- **Profile** : Représente un profil utilisateur, étendant le modèle de base
  `User` pour inclure des informations supplémentaires spécifiques à
  l'application.

Les modèles sont utilisés pour interagir avec la base de données et sont
associés aux tables de la base de données via les options de métadonnées.
"""

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    """
    Modèle représentant un profil utilisateur.

    Ce modèle étend le modèle utilisateur de Django en ajoutant un champ pour
    la ville favorite de l'utilisateur.

    Attributs :
    - **user** (`OneToOneField`) : Une relation un-à-un avec le modèle
      `User`. Ce champ est obligatoire et sera supprimé si l'utilisateur
      associé est supprimé.
    - **favorite_city** (`CharField`) : Le nom de la ville favorite de
      l'utilisateur. Ce champ est optionnel et peut être laissé vide.

    Méthodes :
    - **__str__()** : Retourne le nom d'utilisateur associé au profil comme
      représentation en chaîne de caractères du profil.

    Métadonnées :
    - **db_table** (`str`) : Nom de la table dans la base de données. Défini
      comme "oc_lettings_site_profile".
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères du profil utilisateur.

        Cette méthode renvoie le nom d'utilisateur associé au profil comme
        une chaîne de caractères. Elle est utilisée pour afficher une
        représentation lisible de l'objet `Profile` dans les interfaces
        administratives et autres contextes où une chaîne de caractères est
        nécessaire.

        Retourne :
        - **str** : Le nom d'utilisateur du profil, qui est une représentation
          textuelle de l'objet `Profile`.
        """
        return self.user.username

    class Meta:
        """
        Classe interne de configuration pour le modèle `Profile`.

        Cette classe interne `Meta` est utilisée pour définir des options de
        métadonnées pour le modèle `Profile`. Les options définies ici affectent
        le comportement et la représentation du modèle dans la base de données
        et dans l'interface d'administration Django.

        Attributs :
        - **db_table** (`str`) : Nom de la table dans la base de données qui sera
          utilisée pour stocker les instances du modèle. Dans ce cas, la table
          est nommée "oc_lettings_site_profile".
        """
        db_table = "oc_lettings_site_profile"
