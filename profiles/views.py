"""
views.py

Ce module contient les vues pour l'application de gestion des profils.

Vues disponibles:
    - index: Affiche la liste de tous les profils.
    - profile: Affiche les détails d'un profil spécifique
    basé sur le nom d'utilisateur.
"""

from django.shortcuts import render, get_object_or_404
from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque,
# quis dictum lacus d
def index(request):
    """
    Vue pour afficher la liste des profils des utilisateurs.

    Cette vue récupère tous les profils d'utilisateur à partir
    de la base de données et les passe au modèle
    `profiles/index.html` pour les afficher.
    La liste des profils est envoyée dans le contexte sous la clé
    `profiles_list`.

    Paramètres :
    - request (HttpRequest) : L'objet requête contenant
    les informations sur la requête HTTP effectuée.

    Retourne :
    - HttpResponse : Une réponse HTTP rendue à partir du modèle
    `profiles/index.html`, contenant la liste des profils des utilisateurs.
    """
    profiles_list = Profile.objects.all()
    context = {"profiles_list": profiles_list}
    return render(request, "profiles/index.html", context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac
# laoreet neque quis, pellentesque dui. Nullam facilisis pharetra vulputate.
# Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue.
# Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Vue pour afficher les détails d'un profil utilisateur spécifique.

    Cette vue récupère un profil utilisateur spécifique en fonction du nom
    d'utilisateur (`username`) et passe
    les détails de ce profil au modèle `profiles/profile.html` pour les afficher.
    Les informations du profil
    sont envoyées dans le contexte sous la clé `profile`.

    Paramètres :
    - request (HttpRequest) : L'objet requête contenant les informations
    sur la requête HTTP effectuée.
    - username (str) : Le nom d'utilisateur du profil dont les détails
    doivent être affichés.

    Retourne :
    - HttpResponse : Une réponse HTTP rendue à partir du modèle
    `profiles/profile.html`, contenant les détails du profil utilisateur.
    """

    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
