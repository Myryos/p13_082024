"""
view.py

Ce module contient les vues pour l'application de gestion des locations.

Vues disponibles:
    - lettings_index: Affiche la liste des locations.
    - letting: Affiche les détails d'une location spécifique.
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

    Cette vue récupère toutes les annonces de location présentes dans
    la base de données et les passe au modèle
    `lettings/index.html` pour les afficher. La liste des annonces
    est envoyée dans le contexte sous la clé `lettings_list`.

    Paramètres :
    - request (HttpRequest) : L'objet requête contenant les informations
    sur la requête HTTP effectuée.

    Retourne :
    - HttpResponse : Une réponse HTTP rendue à partir du modèle
    `lettings/index.html`, contenant la liste des annonces de location.
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

    Cette vue récupère une annonce de location spécifique à partir
    de son identifiant (`letting_id`) et passe les
    détails de cette annonce au modèle `lettings/letting.html`
    pour les afficher. Les informations de l'annonce
    sont envoyées dans le contexte sous les clés `title` et `address`.

    Paramètres :
    - request (HttpRequest) : L'objet requête contenant les informations
    sur la requête HTTP effectuée.
    - letting_id (int) : L'identifiant de l'annonce de location dont
    les détails doivent être affichés.

    Retourne :
    - HttpResponse : Une réponse HTTP rendue à partir du modèle
    `lettings/letting.html`, contenant les détails de l'annonce de location.
    """
    letting = get_object_or_404(Letting, pk=letting_id)
    context = {
        "title": letting.title,
        "address": letting.address,
    }
    return render(request, "lettings/letting.html", context)
