"""
Factories pour les modèles Address, Letting, User, et Profile.

Ce fichier définit des classes de factory pour générer des instances des modèles
`Address`, `Letting`, `User`, et `Profile` à des fins de test.
Les factories simplifient la création d'objets avec des
données réalistes et cohérentes pour les tests unitaires.

Classes :
- `AddressFactory` : Génère des instances du modèle `Address`.
- `LettingFactory` : Génère des instances du modèle `Letting` avec une adresse associée.
- `UserFactory` : Génère des instances du modèle `User`.
- `ProfileFactory` : Génère des instances du modèle `Profile`, avec un utilisateur associé.
"""

import factory
from django.contrib.auth.models import User
from lettings.models import Letting, Address
from profiles.models import Profile


class AddressFactory(factory.django.DjangoModelFactory):
    """
    Factory pour le modèle `Address`.

    Cette classe génère des instances du modèle `Address` avec des données réalistes
    pour chaque champ, y compris le numéro de bâtiment, la rue, la ville, l'état,
    le code postal et le code pays (ISO).

    Attributs :
    - `number` : Numéro de bâtiment, généré par Faker.
    - `street` : Nom de la rue, généré par Faker.
    - `city` : Nom de la ville, généré par Faker.
    - `state` : Abréviation de l'état, générée par Faker.
    - `zip_code` : Code postal, généré par Faker.
    - `country_iso_code` : Code ISO du pays, par défaut "USA".
    """

    class Meta:
        model = Address

    number = factory.Faker("building_number")
    street = factory.Faker("street_name")
    city = factory.Faker("city")
    state = factory.Faker("state_abbr")
    zip_code = factory.Faker("zipcode")
    country_iso_code = "USA"


class LettingFactory(factory.django.DjangoModelFactory):
    """
    Factory pour le modèle `Letting`.

    Cette classe génère des instances du modèle `Letting`, qui inclut un titre
    généré aléatoirement et une adresse associée générée par `AddressFactory`.

    Attributs :
    - `title` : Titre de l'annonce, généré par Faker.
    - `address` : Instance d'`Address` associée, générée par `AddressFactory`.
    """

    class Meta:
        model = Letting

    title = factory.Faker("sentence", nb_words=3)
    address = factory.SubFactory(AddressFactory)


class UserFactory(factory.django.DjangoModelFactory):
    """
    Factory pour le modèle `User`.

    Cette classe génère des instances du modèle `User` avec un nom
    d'utilisateur aléatoire généré par Faker.

    Attributs :
    - `username` : Nom d'utilisateur, généré par Faker.
    """

    class Meta:
        model = User

    username = factory.Faker("user_name")


class ProfileFactory(factory.django.DjangoModelFactory):
    """
    Factory pour le modèle `Profile`.

    Cette classe génère des instances du modèle `Profile`, qui inclut un utilisateur
    associé généré par `UserFactory` et une ville favorite générée aléatoirement.

    Attributs :
    - `user` : Instance de `User` associée, générée par `UserFactory`.
    - `favorite_city` : Ville favorite, générée par Faker.
    """

    class Meta:
        model = Profile

    user = factory.SubFactory(UserFactory)
    favorite_city = factory.Faker("city")
