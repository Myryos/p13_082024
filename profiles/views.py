"""
views.py
========

Ce module contient les vues pour l'application de gestion des profils.

Vues disponibles:
-----------------
- ``index`` : Affiche la liste de tous les profils.
- ``profile`` : Affiche les détails d'un profil spécifique basé sur le nom d'utilisateur.
"""

from django.shortcuts import render, get_object_or_404
from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex,
# sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque,
# quis dictum lacus d
def index(request):
    """
    Affiche la liste des profils utilisateurs.

    Récupère tous les profils et les passe au modèle `profiles/index.html` pour affichage.
    La liste des profils est envoyée dans le contexte sous la clé `profiles_list`.

    Paramètres :
    - ``request`` (HttpRequest) : La requête HTTP effectuée.

    Retourne :
    - ``HttpResponse`` : Réponse HTTP contenant la liste des profils.
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
    Affiche les détails d'un profil spécifique.

    Récupère un profil utilisateur en fonction du nom d'utilisateur et le passe au modèle
    `profiles/profile.html` pour affichage. Le profil est envoyé dans le contexte sous la
    clé ``profile``.

    Paramètres :
    - ``request`` (HttpRequest) : La requête HTTP effectuée.
    - ``username`` (str) : Le nom d'utilisateur du profil à afficher.

    Retourne :
    - ``HttpResponse`` : Réponse HTTP contenant les détails du profil utilisateur.
    """

    profile = get_object_or_404(Profile, user__username=username)
    context = {"profile": profile}
    return render(request, "profiles/profile.html", context)
