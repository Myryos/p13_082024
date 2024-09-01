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
from django.contrib.auth.models import User
from .models import Profile


@pytest.mark.django_db
def test_index_view_success(client, mocker):
    """
    Teste la vue index pour vérifier le comportement lorsque des
    profils sont disponibles.
    """
    # Mock pour la vue index
    mock_profiles = mocker.patch(
        "profiles.views.Profile.objects.all",
        return_value=[
            Profile(user=User(username="testuser1"), favorite_city="City1"),
            Profile(user=User(username="testuser2"), favorite_city="City2"),
        ],
    )

    url_index = reverse("profiles_index")
    response_index = client.get(url_index)

    assert response_index.status_code == 200
    assert "profiles_list" in response_index.context
    assert "testuser1" in response_index.content.decode()
    assert "testuser2" in response_index.content.decode()
    mock_profiles.assert_called_once()


@pytest.mark.django_db
def test_index_view_no_profiles(client, mocker):
    """
    Teste la vue index pour vérifier le comportement
    lorsqu'aucun profil n'est disponible.
    """
    # Mock pour la vue index avec une liste vide
    mock_profiles = mocker.patch("profiles.views.Profile.objects.all", return_value=[])

    url_index = reverse("profiles_index")
    response_index = client.get(url_index)

    print("Contexte de réponse pour le sad path:", response_index.context)
    print("Contenu de la réponse pour le sad path:", response_index.content.decode())

    assert response_index.status_code == 200
    assert "profiles_list" in response_index.context
    assert len(response_index.context["profiles_list"]) == 0
    assert "<p>No profiles are available.</p>" in response_index.content.decode()
    mock_profiles.assert_called_once()


@pytest.mark.django_db
def test_profile_view_success(client, mocker):
    """
    Teste la vue profile pour vérifier le comportement
    lorsque le profil est disponible.
    """
    # Création d'un utilisateur et d'un profil pour le test
    user = User.objects.create(username="testuser")
    profile = Profile.objects.create(user=user, favorite_city="Test City")

    # Mock pour la vue profile
    mocker.patch("profiles.views.Profile.objects.get", return_value=profile)

    url_profile = reverse("profile", kwargs={"username": "testuser"})
    response_profile = client.get(url_profile)

    # Assurez-vous que la réponse est correcte
    assert response_profile.status_code == 200
    assert "profile" in response_profile.context
    assert "Test City" in response_profile.content.decode()


@pytest.mark.django_db
def test_profile_view_not_found(client, mocker):
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
    # Crée un utilisateur valide
    user = User.objects.create(username="testuser")

    # Crée un profil valide associé à cet utilisateur
    profile = Profile.objects.create(user=user, favorite_city="Paris")

    # Vérifie que le profil est bien créé
    assert profile.user == user
    assert profile.favorite_city == "Paris"
    assert (
        str(profile) == "testuser"
    )  # Utilise la méthode __str__() pour vérifier la représentation en chaîne de caractères
