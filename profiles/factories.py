"""
Factories pour les modèles User et Profile.

Ce fichier définit des classes de factory pour générer des instances des
modèles `User` et `Profile` à des fins de test. Les factories sont
utilisées pour créer des objets de manière simple et cohérente dans les
tests unitaires, en générant des données réalistes sans avoir à les créer
manuellement.

Classes :
- **UserFactory** : Génère des instances du modèle `User`.
- **ProfileFactory** : Génère des instances du modèle `Profile`, avec un
  utilisateur associé généré par `UserFactory`.
"""

import factory
from django.contrib.auth.models import User
from .models import Profile


class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory pour le modèle `User`.

    Cette classe génère des instances de l'utilisateur Django par défaut.
    Chaque utilisateur créé a un nom d'utilisateur unique et une adresse
    email dérivée de ce nom d'utilisateur.

    Attributs :
    - **username** : Un nom d'utilisateur unique généré automatiquement.
    - **first_name** : Prénom de l'utilisateur, par défaut "John".
    - **last_name** : Nom de famille de l'utilisateur, par défaut "Doe".
    - **email** : Adresse email de l'utilisateur, générée automatiquement à
      partir du nom d'utilisateur.
    """

    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    first_name = "John"
    last_name = "Doe"
    email = factory.LazyAttribute(lambda obj: f"{obj.username}@example.com")


class ProfileFactory(factory.django.DjangoModelFactory):
    """
    Factory pour le modèle `Profile`.

    Cette classe génère des instances du modèle `Profile`, qui inclut un
    utilisateur associé généré par `UserFactory` et une ville favorite
    choisie de manière aléatoire.

    Attributs :
    - **user** : Une instance de `User` associée, générée par `UserFactory`.
    - **favorite_city** : Une ville favorite choisie aléatoirement à l'aide
      de Faker.
    """

    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    favorite_city = factory.Faker("city")
