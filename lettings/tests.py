"""
Tests des vues liées aux annonces de location.

Ce module contient des tests unitaires pour vérifier le bon
fonctionnement des vues associées aux annonces de location (`lettings`).
Les tests sont réalisés à l'aide de `pytest` et `pytest-django`,
et utilisent `factory_boy` pour générer des objets de test de manière réaliste.

Vues testées :
- `lettings_index` : Affiche la liste des annonces de location disponibles.
- `letting` : Affiche les détails d'une annonce de location spécifique.

Les tests vérifient les aspects suivants :
- La vue `lettings_index` affiche correctement la liste des annonces de
location et traite le cas où aucune annonce n'est disponible
(scénario de chemin malheureux).
- La vue `letting` affiche correctement les détails d'une annonce spécifique
et gère les erreurs lorsque l'annonce demandée n'existe pas.
"""

import pytest
from django.urls import reverse
from .factories import LettingFactory


@pytest.mark.django_db
def test_index_view(client):
    """
    Teste la vue index pour vérifier que la liste des annonces de location
    s'affiche correctement.
    """
    # Création de deux locations avec factory_boy
    LettingFactory(title="Nice Apartment")
    LettingFactory(title="Cozy House")

    url = reverse("lettings_index")
    response = client.get(url)

    # Vérifiez le contenu du contexte et des données
    assert response.status_code == 200
    assert "lettings_list" in response.context
    assert len(response.context["lettings_list"]) == 2
    assert "Nice Apartment" in response.content.decode()
    assert "Cozy House" in response.content.decode()


@pytest.mark.django_db
def test_letting_view(client):
    """
    Teste la vue 'letting' pour vérifier que les détails
    d'une annonce de location sont correctement affichés.
    """
    # Création d'une location avec factory_boy
    letting = LettingFactory(title="Cozy House")

    url = reverse("letting", kwargs={"letting_id": letting.id})
    response = client.get(url)

    # Vérifiez le contenu du contexte et des données
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
    Teste la vue index pour vérifier le comportement lorsqu'aucune
    annonce de location n'est disponible.
    """
    url = reverse("lettings_index")
    response = client.get(url)

    # Vérifiez le contenu du contexte et des données pour le sad path
    assert response.status_code == 200
    assert "lettings_list" in response.context
    assert len(response.context["lettings_list"]) == 0
    assert "<p>No lettings are available.</p>" in response.content.decode()


@pytest.mark.django_db
def test_letting_view_sad_path(client):
    """
    Teste la vue 'letting' pour vérifier le comportement
    lorsqu'une annonce de location n'est pas trouvée.
    """
    url = reverse("letting", kwargs={"letting_id": 999})  # ID inexistant

    response = client.get(url)

    # Vérification du code de statut 404
    assert response.status_code == 404
