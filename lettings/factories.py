"""
Factories pour les modèles Address et Letting.

Ce fichier définit des classes de factory pour générer des instances des modèles
`Address` et `Letting` à des fins de test. Ces factories utilisent le module
`factory_boy` pour créer des objets avec des données réalistes, permettant ainsi
de simplifier les tests unitaires et d'intégration.

Classes :
- `AddressFactory` : Génère des instances du modèle `Address`.
- `LettingFactory` : Génère des instances du modèle `Letting` avec une adresse
  associée.
"""

import factory
from .models import Address, Letting


class AddressFactory(factory.django.DjangoModelFactory):
    """
    Factory pour le modèle `Address`.

    Cette classe génère des instances du modèle `Address` avec des données
    réalistes pour chaque champ, y compris le numéro de bâtiment, la rue, la
    ville, l'état, le code postal, et le code pays (ISO).

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
