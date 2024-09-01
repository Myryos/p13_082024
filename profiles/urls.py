"""
urls.py

Ce module définit les URL pour l'application de gestion des profils.

Les URL suivantes sont disponibles :
- / : Affiche la liste de tous les profils. (Nom de l'URL : 'profiles_index')
- /<username>/ : Affiche les détails d'un profil spécifique basé
sur le nom d'utilisateur. (Nom de l'URL : 'profile')

Les vues associées sont définies dans le module `views.py`.

Exemple d'utilisation des URL :
- La route vide ('') est associée à la vue `index` pour afficher
la liste des profils.
- La route avec un nom d'utilisateur ('<str:username>/') est
associée à la vue `profile` pour afficher les détails d'un profil spécifique.
"""

from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="profiles_index"),
    path("<str:username>/", view=views.profile, name="profile"),
]
