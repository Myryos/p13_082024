========================
Lettings Tests
========================

Ce module contient des tests unitaires pour les vues définies dans `views.py` de l'application
de gestion des annonces de location. Les tests sont réalisés à l'aide de `pytest` et `pytest-django`.

Les tests vérifient les aspects suivants :
- La vue `index` rend correctement la liste des annonces de location et affiche les données attendues.
- La vue `letting` affiche les détails corrects pour une annonce spécifique et gère les cas où l'annonce n'existe pas.

.. pytest:: lettings.tests
   :addopts: --maxfail=5 --disable-warnings -q
