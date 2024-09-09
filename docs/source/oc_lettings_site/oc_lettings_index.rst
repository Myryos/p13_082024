========================
oc_letting_site Documentation
========================

Bienvenue dans la documentation de l'application `oc_letting_site`. Cette documentation couvre divers aspects de l'application, y compris les modèles, les vues, les URL, les tests, et les factories. Vous trouverez ci-dessous des liens vers les différentes sections de la documentation.

.. toctree::
   :maxdepth: 2
   :caption: Contenu de la Documentation :

   index_tests

========================
Tests
========================

Ce module contient des tests unitaires pour les vues principales de l'application `oc_letting_site`. Les tests sont réalisés à l'aide de `pytest` et `pytest-django`, en utilisant `factory_boy` pour générer des objets de test de manière réaliste.

Les tests vérifient les aspects suivants :
- La vue `index` rend correctement la page d'accueil et contient le contenu attendu.
- La vue `lettings_index` affiche correctement les annonces de location et gère le cas où aucune annonce n'est disponible.
- La vue `profiles_index` affiche correctement les profils utilisateur et gère le cas où aucun profil n'est disponible.
- Les routes non définies sont correctement traitées avec une erreur 404.

.. toctree::
   :maxdepth: 1
   :caption: Voir les détails des tests :

   oc_lettings_test
