import pytest
from django.urls import reverse
from .models import Address, Letting


@pytest.mark.django_db
def test_index_view(mocker, client):
    """
    Teste la vue index pour vérifier que la liste des annonces de location s'affiche correctement.
    """
    # Création des objets pour le test
    address1 = Address.objects.create(
        number=123,
        street="Main St",
        city="Testville",
        state="TS",
        zip_code=12345,
        country_iso_code="USA",
    )
    address2 = Address.objects.create(
        number=456,
        street="Second St",
        city="Testtown",
        state="TT",
        zip_code=67890,
        country_iso_code="USA",
    )
    letting1 = Letting.objects.create(title="Nice Apartment", address=address1)
    letting2 = Letting.objects.create(title="Cozy House", address=address2)

    # Mock pour la méthode all() de Letting
    mock_lettings_all = mocker.patch("lettings.models.Letting.objects.all")
    mock_lettings_all.return_value = [letting1, letting2]

    url = reverse("lettings_index")
    response = client.get(url)

    # Vérifiez le contenu du contexte et des données
    print("Contexte de réponse:", response.context)
    print("Contenu de la réponse:", response.content.decode())

    # Assurez-vous que la vue renvoie le bon code de statut et le bon contexte
    assert response.status_code == 200
    assert "lettings_list" in response.context
    assert len(response.context["lettings_list"]) == 2
    assert "Nice Apartment" in response.content.decode()
    assert "Cozy House" in response.content.decode()


@pytest.mark.django_db
def test_letting_view(mocker, client):
    """
    Teste la vue 'letting' pour vérifier que les détails
    d'une annonce de location sont correctement affichés.
    """
    # Création des objets pour le test
    address = Address.objects.create(
        number=123,
        street="Main St",
        city="Testville",
        state="TS",
        zip_code=12345,
        country_iso_code="USA",
    )
    letting = Letting.objects.create(title="Cozy House", address=address)

    # Mock pour la méthode get() de Letting
    mock_letting_get = mocker.patch("lettings.models.Letting.objects.get")
    mock_letting_get.return_value = letting

    # Test du chemin heureux (happy path)
    url = reverse("letting", kwargs={"letting_id": letting.id})
    response = client.get(url)

    # Vérifiez le contenu du contexte et des données
    print("Contexte de réponse:", response.context)
    print("Contenu de la réponse:", response.content.decode())

    # Assurez-vous que la vue renvoie le bon code de statut et le bon contexte
    assert response.status_code == 200
    assert "title" in response.context
    assert "address" in response.context
    assert response.context["title"] == letting.title
    assert response.context["address"] == letting.address
    assert "Cozy House" in response.content.decode()
    assert "Main St" in response.content.decode()


@pytest.mark.django_db
def test_index_view_sad_path(mocker, client):
    """
    Teste la vue index pour vérifier le comportement
    lorsqu'aucune annonce de location n'est disponible.
    """
    # Mock pour la méthode all() de Letting qui retourne une liste vide
    mock_lettings_all = mocker.patch("lettings.models.Letting.objects.all")
    mock_lettings_all.return_value = []

    url = reverse("lettings_index")
    response = client.get(url)

    # Vérifiez le contenu du contexte et des données pour le sad path
    print("Contexte de réponse pour le sad path:", response.context)
    print("Contenu de la réponse pour le sad path:", response.content.decode())

    # Assurez-vous que la vue renvoie le bon code de statut et le bon contexte
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
    # URL vers la vue avec un ID inexistant
    url = reverse("letting", kwargs={"letting_id": 999})  # ID inexistant

    # Test pour s'assurer que la réponse a un statut 404
    response = client.get(url)

    # Vérification du code de statut 404
    assert response.status_code == 404
