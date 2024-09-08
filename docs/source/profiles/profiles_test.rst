========================
Profiles Tests
========================

Ce module contient des tests unitaires pour les vues définies dans `views.py` de l'application de gestion des profils. Les tests sont réalisés à l'aide de `pytest` et `pytest-django`.

Les tests vérifient les aspects suivants :
- La vue `index` rend correctement la liste des profils et affiche les données attendues.
- La vue `profile` affiche les détails corrects pour un utilisateur spécifique et gère les cas où l'utilisateur n'existe pas.

.. pytest:: profiles.tests
   :addopts: --maxfail=5 --disable-warnings -q
