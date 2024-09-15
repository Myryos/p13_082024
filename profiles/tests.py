"""
Tests des vues pour l'application de gestion des profils.

Ce module contient des tests unitaires pour les vues définies dans `views.py`.
Les tests utilisent `pytest` et `pytest-django`.

Vues testées :
--------------

- ``index`` : Teste la vue affichant la liste des profils.
- ``profile`` : Teste la vue affichant les détails d'un profil utilisateur.

Les tests vérifient :
---------------------

- La vue ``index`` rend la liste des profils avec les données attendues.
- La vue ``profile`` affiche les détails corrects d'un utilisateur et gère
  les cas d'absence de profil.
"""

import pytest
from django.urls import reverse
from .factories import ProfileFactory


@pytest.mark.django_db
def test_index_view_success(client):
    """
    Teste la vue ``index`` lorsque des profils sont disponibles.
    """
    # Création de deux profils avec factory_boy
    ProfileFactory(user__username="testuser1", favorite_city="City1")
    ProfileFactory(user__username="testuser2", favorite_city="City2")

    url_index = reverse("profiles_index")
    response_index = client.get(url_index)

    assert response_index.status_code == 200
    assert "profiles_list" in response_index.context
    assert "testuser1" in response_index.content.decode()
    assert "testuser2" in response_index.content.decode()


@pytest.mark.django_db
def test_index_view_no_profiles(client):
    """
    Teste la vue ``index`` lorsque aucun profil n'est disponible.
    """
    url_index = reverse("profiles_index")
    response_index = client.get(url_index)

    assert response_index.status_code == 200
    assert "profiles_list" in response_index.context
    assert len(response_index.context["profiles_list"]) == 0
    assert "<p>No profiles are available.</p>" in response_index.content.decode()


@pytest.mark.django_db
def test_profile_view_success(client):
    """
    Teste la vue ``profile`` lorsque le profil est disponible.
    """
    # Création d'un profil pour le test avec factory_boy
    profile = ProfileFactory(user__username="testuser", favorite_city="Test City")

    url_profile = reverse("profile", kwargs={"username": profile.user.username})
    response_profile = client.get(url_profile)

    assert response_profile.status_code == 200
    assert "profile" in response_profile.context
    assert "Test City" in response_profile.content.decode()


@pytest.mark.django_db
def test_profile_view_not_found(client):
    """
    Teste la vue ``profile`` lorsqu'aucun profil n'est trouvé.
    """
    url_profile = reverse("profile", kwargs={"username": "nonexistentuser"})
    response_profile = client.get(url_profile)

    assert response_profile.status_code == 404


@pytest.mark.django_db
def test_profile_creation():
    """
    Teste la création d'un profil utilisateur avec des données valides.
    """
    # Utilisation de factory_boy pour créer un utilisateur et un profil
    profile = ProfileFactory(user__username="testuser", favorite_city="Paris")

    assert profile.user.username == "testuser"
    assert profile.favorite_city == "Paris"
    assert str(profile) == "testuser"
