"""
Tests des vues pour l'application de gestion des profils.

Ce module contient des tests unitaires pour les vues définies dans
`views.py`. Les tests sont réalisés à l'aide de `pytest` et `pytest-django`.

Vues testées :
- **index** : Teste la vue qui affiche la liste de tous les profils.
- **profile** : Teste la vue qui affiche les détails d'un profil utilisateur
  spécifique.

Les tests vérifient les aspects suivants :
- La vue `index` rend correctement la liste des profils et affiche les données
  attendues.
- La vue `profile` affiche les détails corrects pour un utilisateur spécifique
  et gère les cas où l'utilisateur n'existe pas.
"""

import pytest
from django.urls import reverse
from .factories import ProfileFactory


@pytest.mark.django_db
def test_index_view_success(client):
    """
    Teste la vue ``index`` pour vérifier le comportement lorsque des profils
    sont disponibles.

    Cette fonction :
    - Crée deux profils avec `factory_boy`.
    - Récupère l'URL pour la vue ``index``.
    - Vérifie que la réponse HTTP est correcte et que les profils sont bien
      affichés.
    """
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
    Teste la vue ``index`` pour vérifier le comportement lorsqu'aucun profil
    n'est disponible.

    Cette fonction :
    - Récupère l'URL pour la vue ``index``.
    - Vérifie que la réponse HTTP est correcte et que le message indiquant
      l'absence de profils est affiché.
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
    Teste la vue ``profile`` pour vérifier le comportement lorsque le profil
    est disponible.

    Cette fonction :
    - Crée un profil pour le test avec `factory_boy`.
    - Récupère l'URL pour la vue ``profile`` en utilisant le nom d'utilisateur
      du profil.
    - Vérifie que la réponse HTTP est correcte et que les détails du profil
      sont affichés correctement.
    """
    profile = ProfileFactory(user__username="testuser", favorite_city="Test City")

    url_profile = reverse("profile", kwargs={"username": profile.user.username})
    response_profile = client.get(url_profile)

    assert response_profile.status_code == 200
    assert "profile" in response_profile.context
    assert "Test City" in response_profile.content.decode()


@pytest.mark.django_db
def test_profile_view_not_found(client):
    """
    Teste la vue ``profile`` pour vérifier le comportement lorsqu'aucun profil
    n'est trouvé.

    Cette fonction :
    - Récupère l'URL pour la vue ``profile`` en utilisant un nom d'utilisateur
      inexistant.
    - Vérifie que la réponse HTTP est une erreur 404 lorsque le profil n'est
      pas trouvé.
    """
    url_profile = reverse("profile", kwargs={"username": "nonexistentuser"})
    response_profile = client.get(url_profile)

    assert response_profile.status_code == 404


@pytest.mark.django_db
def test_profile_creation():
    """
    Teste la création d'un profil utilisateur avec des données valides.

    Cette fonction :
    - Utilise `factory_boy` pour créer un utilisateur et un profil avec des
      données valides.
    - Vérifie que les données du profil sont correctement créées et que la
      représentation du profil est correcte.
    """
    profile = ProfileFactory(user__username="testuser", favorite_city="Paris")

    assert profile.user.username == "testuser"
    assert profile.favorite_city == "Paris"
    assert str(profile) == "testuser"
