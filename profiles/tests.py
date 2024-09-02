"""
Tests des vues pour l'application de gestion des profils.

Ce module contient des tests unitaires pour les vues définies dans `views.py`.
Les tests sont réalisés à l'aide de `pytest` et `pytest-django`.

Vues testées :
- index : Teste la vue qui affiche la liste de tous les profils.
- profile : Teste la vue qui affiche les détails d'un profil utilisateur
spécifique.

Les tests vérifient les aspects suivants :
- La vue `index` rend correctement la liste des profils et affiche
les données attendues.
- La vue `profile` affiche les détails corrects pour un utilisateur
spécifique et gère les cas où l'utilisateur n'existe pas.
"""

import pytest
from django.urls import reverse
from .factories import ProfileFactory


@pytest.mark.django_db
def test_index_view_success(client):
    """
    Teste la vue index pour vérifier le comportement lorsque des
    profils sont disponibles.
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
    Teste la vue index pour vérifier le comportement
    lorsqu'aucun profil n'est disponible.
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
    Teste la vue profile pour vérifier le comportement
    lorsque le profil est disponible.
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
    Teste la vue profile pour vérifier le comportement
    lorsqu'aucun profil n'est trouvé.
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
