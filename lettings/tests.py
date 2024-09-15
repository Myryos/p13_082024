"""
Tests des vues liées aux annonces de location.

Ce module contient des tests unitaires pour vérifier le bon fonctionnement des
vues associées aux annonces de location (`lettings`). Les tests utilisent `pytest`
et `pytest-django`, ainsi que `factory_boy` pour générer des objets de test réalistes.

Vues testées :
- `lettings_index` : Affiche la liste des annonces de location disponibles.
- `letting` : Affiche les détails d'une annonce de location spécifique.

Les tests vérifient :
- Que la vue `lettings_index` affiche correctement les annonces et gère le cas
  sans annonces.
- Que la vue `letting` affiche les détails d'une annonce spécifique et gère les
  erreurs si l'annonce n'existe pas.
"""

import pytest
from django.urls import reverse
from .factories import LettingFactory


@pytest.mark.django_db
def test_index_view(client):
    """
    Teste la vue `lettings_index` pour vérifier l'affichage des annonces de location.
    """
    # Création de deux annonces avec factory_boy
    LettingFactory(title="Nice Apartment")
    LettingFactory(title="Cozy House")

    url = reverse("lettings_index")
    response = client.get(url)

    # Vérifie le contenu du contexte et des données
    assert response.status_code == 200
    assert "lettings_list" in response.context
    assert len(response.context["lettings_list"]) == 2
    assert "Nice Apartment" in response.content.decode()
    assert "Cozy House" in response.content.decode()


@pytest.mark.django_db
def test_letting_view(client):
    """
    Teste la vue `letting` pour vérifier l'affichage des détails d'une annonce.
    """
    # Création d'une annonce avec factory_boy
    letting = LettingFactory(title="Cozy House")

    url = reverse("letting", kwargs={"letting_id": letting.id})
    response = client.get(url)

    # Vérifie le contenu du contexte et des données
    assert response.status_code == 200
    assert "title" in response.context
    assert "address" in response.context
    assert response.context["title"] == letting.title
    assert response.context["address"] == letting.address
    assert "Cozy House" in response.content.decode()
    assert letting.address.street in response.content.decode()


@pytest.mark.django_db
def test_index_view_sad_path(client):
    """
    Teste la vue `lettings_index` lorsque aucune annonce de location n'est disponible.
    """
    url = reverse("lettings_index")
    response = client.get(url)

    # Vérifie le contenu pour le cas sans annonces
    assert response.status_code == 200
    assert "lettings_list" in response.context
    assert len(response.context["lettings_list"]) == 0
    assert "<p>No lettings are available.</p>" in response.content.decode()


@pytest.mark.django_db
def test_letting_view_sad_path(client):
    """
    Teste la vue `letting` pour vérifier le comportement si l'annonce n'est pas trouvée.
    """
    url = reverse("letting", kwargs={"letting_id": 999})  # ID inexistant

    response = client.get(url)

    # Vérifie le code de statut 404 pour une annonce inexistante
    assert response.status_code == 404
