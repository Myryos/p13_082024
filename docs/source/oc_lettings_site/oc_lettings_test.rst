========================
oc_letting_site Tests
========================

Ce module contient des tests unitaires pour les vues principales de l'application `oc_letting_site`. Les tests sont réalisés à l'aide de `pytest` et `pytest-django`, en utilisant `factory_boy` pour générer des objets de test de manière réaliste.

Les tests vérifient les aspects suivants :
- La vue `index` rend correctement la page d'accueil et contient le contenu attendu.
- La vue `lettings_index` affiche correctement les annonces de location et gère le cas où aucune annonce n'est disponible.
- La vue `profiles_index` affiche correctement les profils utilisateur et gère le cas où aucun profil n'est disponible.
- Les routes non définies sont correctement traitées avec une erreur 404.

Vues testées :
- **index** : Teste la page d'accueil principale de l'application.
- **lettings_index** : Teste la vue affichant la liste des annonces de location.
- **profiles_index** : Teste la vue affichant la liste des profils utilisateur.

.. pytest:: oc_letting_site.tests
   :addopts: --maxfail=5 --disable-warnings -q
