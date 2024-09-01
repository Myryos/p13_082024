"""
test.py

"""

import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_view_success(client):
    """
    Teste la vue `index` pour vérifier que la page est correctement
    rendue et renvoie un code de statut 200.

    Ce test vérifie les éléments suivants :
    - La réponse HTTP renvoyée a un code de statut 200.
    - Le template utilisé pour rendre la vue est bien 'index.html'.
    - Le contenu de la page contient le texte attendu,
    ce qui indique que la page a été rendue correctement.
    """
    url = reverse("index")  # Utilisez le nom de l'URL défini dans vos routes
    response = client.get(url)

    # Vérifiez que la réponse est OK
    assert response.status_code == 200

    # Vérifiez que le template utilisé est 'index.html'
    assert "index.html" in [t.name for t in response.templates]

    # Vérifiez le contenu de la page (assurez-vous que
    # ce texte correspond à ce que vous attendez dans votre template)
    assert (
        "Welcome to Holiday Homes" in response.content.decode()
    )  # Remplacez par le texte réel


@pytest.mark.django_db
def test_letting_route(client):
    """
    Teste la route `lettings_index` pour vérifier
    qu'elle redirige correctement vers les URLs définies dans l'app 'lettings'.

    Ce test vérifie les éléments suivants :
    - La réponse HTTP renvoyée a un code de statut 200.
    - Le contenu de la page contient le texte attendu,
    ce qui indique que la page a été rendue correctement.
    """
    url = reverse("lettings_index")
    response = client.get(url)
    assert response.status_code == 200
    assert "Lettings" in response.content.decode()


@pytest.mark.django_db
def test_profiles_route(client):
    """
    Teste la route `profiles_index` pour vérifier
    qu'elle redirige correctement vers les URLs définies dans l'app 'profiles'.

    Ce test vérifie les éléments suivants :
    - La réponse HTTP renvoyée a un code de statut 200.
    - Le contenu de la page contient le texte attendu,
    ce qui indique que la page a été rendue correctement.
    """
    url = reverse("profiles_index")
    response = client.get(url)
    assert response.status_code == 200
    assert "Profiles" in response.content.decode()


@pytest.mark.django_db
def test_not_found_route(client):
    """
    Teste une route non définie pour vérifier que le code de statut 404
    est renvoyé.

    Ce test vérifie que la page non existante renvoie une erreur
    404 et que le contenu indique que la page est introuvable.
    """
    message_search = "The page you were looking for could not be found."
    url = "/nonexistent_route/"
    response = client.get(url)
    assert response.status_code == 404
    assert message_search in response.content.decode()


# Tests supplémentaires pour les scénarios malheureux (sad paths)


@pytest.mark.django_db
def test_letting_route_not_found(client, mocker):
    """
    Teste la route `lettings_index` pour vérifier le comportement
    lorsqu'aucune annonce de location n'est disponible.

    Ce test vérifie que la page de la liste des annonces de
    location affiche un message indiquant qu'aucune annonce n'est disponible.
    """
    mock_lettings = mocker.patch("lettings.views.Letting.objects.all", return_value=[])

    url = reverse("lettings_index")
    response = client.get(url)

    assert response.status_code == 200
    assert "No lettings are available" in response.content.decode()
    mock_lettings.assert_called_once()


@pytest.mark.django_db
def test_profiles_route_empty(client, mocker):
    """
    Teste la route `profiles_index` pour vérifier le comportement
    lorsqu'aucun profil n'est disponible.

    Ce test vérifie que la page de la liste des profils affiche
    un message indiquant qu'aucun profil n'est disponible.
    """
    # Mock pour simuler l'absence de profils
    mock_profiles = mocker.patch("profiles.views.Profile.objects.all", return_value=[])

    url = reverse("profiles_index")
    response = client.get(url)

    assert response.status_code == 200
    assert "No profiles are available" in response.content.decode()
    mock_profiles.assert_called_once()
