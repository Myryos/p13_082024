"""
test.py

Tests des vues principales de l'application.

Ce module contient des tests unitaires pour vérifier le bon fonctionnement
des vues principales du projet Django, notamment les vues index, letting,
et profiles. Les tests sont réalisés à l'aide de `pytest` et `pytest-django`,
et utilisent `factory_boy` pour générer des objets de test de manière réaliste.

Vues testées :
- `index` : Teste la page d'accueil principale de l'application.
- `lettings_index` : Teste la vue qui affiche la liste des annonces de location.
- `profiles_index` : Teste la vue qui affiche la liste des profils utilisateur.

Les tests vérifient les aspects suivants :
- La vue `index` est correctement rendue avec le template approprié et
contient le contenu attendu.
- La vue `lettings_index` renvoie un code de statut 200 et affiche
correctement les annonces de location disponibles.
- La vue `profiles_index` renvoie un code de statut 200 et affiche
correctement les profils utilisateurs disponibles.
- Les scénarios malheureux (`sad paths`) sont couverts, incluant les
cas où aucune annonce ou aucun profil n'est disponible,
ainsi que la gestion des routes non définies qui doivent renvoyer une erreur 404.
"""

import pytest
from django.urls import reverse
from .factories import LettingFactory, ProfileFactory


@pytest.mark.django_db
def test_index_view_success(client):
    """
    Teste la vue `index` pour vérifier que la page est correctement
    rendue et renvoie un code de statut 200.
    """
    url = reverse("index")
    response = client.get(url)

    assert response.status_code == 200
    assert "index.html" in [t.name for t in response.templates]
    assert "Welcome to Holiday Homes" in response.content.decode()


@pytest.mark.django_db
def test_letting_route(client):
    """
    Teste la route `lettings_index` pour vérifier
    qu'elle redirige correctement vers les URLs définies dans l'app 'lettings'.
    """
    LettingFactory.create_batch(2)  # Crée deux Lettings
    url = reverse("lettings_index")
    response = client.get(url)

    assert response.status_code == 200
    assert "Lettings" in response.content.decode()


@pytest.mark.django_db
def test_profiles_route(client):
    """
    Teste la route `profiles_index` pour vérifier
    qu'elle redirige correctement vers les URLs définies dans l'app 'profiles'.
    """
    ProfileFactory.create_batch(2)  # Crée deux Profiles
    url = reverse("profiles_index")
    response = client.get(url)

    assert response.status_code == 200
    assert "Profiles" in response.content.decode()


@pytest.mark.django_db
def test_not_found_route(client):
    """
    Teste une route non définie pour vérifier que le code de statut 404
    est renvoyé.
    """
    message_search = "The page you were looking for could not be found."
    url = "/nonexistent_route/"
    response = client.get(url)

    assert response.status_code == 404
    assert message_search in response.content.decode()


@pytest.mark.django_db
def test_letting_route_not_found(client):
    """
    Teste la route `lettings_index` pour vérifier le comportement
    lorsqu'aucune annonce de location n'est disponible.
    """
    url = reverse("lettings_index")
    response = client.get(url)

    assert response.status_code == 200
    assert "No lettings are available" in response.content.decode()


@pytest.mark.django_db
def test_profiles_route_empty(client):
    """
    Teste la route `profiles_index` pour vérifier le comportement
    lorsqu'aucun profil n'est disponible.
    """
    url = reverse("profiles_index")
    response = client.get(url)

    assert response.status_code == 200
    assert "No profiles are available" in response.content.decode()
