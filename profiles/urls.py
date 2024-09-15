"""
urls.py
=======

Ce module définit les URL pour l'application de gestion des profils.

Les URL suivantes sont disponibles :
-------------------------------------

- / : Affiche la liste de tous les profils. (Nom de l'URL : 'profiles_index')
- /<username>/ : Affiche les détails d'un profil spécifique. (Nom de l'URL : 'profile')

Les vues associées sont définies dans `views.py`.

Exemples d'utilisation :
------------------------

- La route '' est associée à la vue ``index`` pour afficher la liste des profils.
- La route '<str:username>/' est associée à la vue ``profile`` pour afficher un
  profil spécifique.
"""

from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="profiles_index"),
    path("<str:username>/", view=views.profile, name="profile"),
]
