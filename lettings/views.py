"""
views.py

Ce module contient les vues pour l'application de gestion des locations.

Vues disponibles :
- `lettings_index` : Affiche la liste des locations.
- `letting` : Affiche les détails d'une location spécifique.
"""

from django.shortcuts import render, get_object_or_404
from .models import Letting


# Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
# Sed non placerat massa. Integer est nunc, pulvinar a
# tempor et, bibendum id arcu. Vestibulum ante ipsum primis in faucibus orci
# luctus et ultrices posuere cubilia curae; Cras eget scelerisque
def index(request):
    """
    Vue pour afficher la liste des annonces de location.

    Récupère toutes les annonces de location de la base de données et les passe
    au modèle `lettings/index.html` pour affichage. La liste des annonces est
    envoyée dans le contexte sous la clé `lettings_list`.

    :param request: Objet requête contenant les informations HTTP.
    :type request: HttpRequest

    :return: Réponse HTTP rendue à partir du modèle `lettings/index.html`, avec
        la liste des annonces de location.
    :rtype: HttpResponse
    """
    lettings_list = Letting.objects.all()
    context = {"lettings_list": lettings_list}
    return render(request, "lettings/index.html", context)


# Cras ultricies dignissim purus, vitae hendrerit ex varius non.
# In accumsan porta nisl id eleifend. Praesent dignissim, odio eu consequat
# pretium, purus urna vulputate arcu, vitae efficitur
#  lacus justo nec purus. Aenean finibus faucibus lectus at porta.
# Maecenas auctor, est ut luctus congue, dui enim mattis enim,
# ac condimentum velit libero in magna. Suspendisse potenti.
# In tempus a nisi sed laoreet.
# Suspendisse porta dui eget sem accumsan interdum.
# Ut quis urna pellentesque justo mattis ullamcorper ac non tellus.
# In tristique mauris eu velit fermentum, tempus pharetra est luctus.
# Vivamus consequat aliquam libero, eget bibendum lorem. Sed non dolor risus.
# Mauris condimentum auctor elementum. Donec quis nisi ligula.
# Integer vehicula tincidunt enim, ac lacinia augue pulvinar sit amet.
def letting(request, letting_id):
    """
    Vue pour afficher les détails d'une annonce de location spécifique.

    Récupère une annonce de location par son identifiant (`letting_id`) et passe
    les détails au modèle `lettings/letting.html`. Les informations sont envoyées
    dans le contexte sous les clés `title` et `address`.

    :param request: Objet requête contenant les informations HTTP.
    :type request: HttpRequest
    :param letting_id: Identifiant de l'annonce dont les détails doivent être
        affichés.
    :type letting_id: int

    :return: Réponse HTTP rendue à partir du modèle `lettings/letting.html`, avec
        les détails de l'annonce.
    :rtype: HttpResponse
    """
    letting = get_object_or_404(Letting, pk=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
