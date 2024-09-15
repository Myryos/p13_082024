"""
urls.py

Ce module définit les URL pour l'application de gestion des annonces (`lettings`).

Les URL disponibles :
- / : Affiche la liste de toutes les annonces. (Nom de l'URL : 'lettings_index')
- /<letting_id>/ : Affiche les détails d'une annonce spécifique par son identifiant.
  (Nom de l'URL : 'letting')

Les vues associées sont définies dans le module `views.py`.

Exemple d'utilisation des URL :
- La route vide ('') est associée à la vue `index` pour afficher la liste des annonces.
- La route avec un identifiant d'annonce ('<int:letting_id>/') est associée à la vue
  `letting` pour afficher les détails d'une annonce spécifique.

Paramètres d'URL :
- `letting_id` (int) : Identifiant unique de l'annonce à afficher.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="lettings_index"),
    path("<int:letting_id>/", view=views.letting, name="letting"),
]
