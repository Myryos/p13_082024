===============================
Technologies et Langages
===============================

Le projet **Orange County Lettings** utilise une combinaison de technologies et de langages pour assurer le bon fonctionnement de l'application. Voici un aperçu des principales technologies et bibliothèques utilisées :

Langages de Programmation
=========================

- **Python** : Le langage principal utilisé pour le développement du projet, version 3.6 ou supérieure.

Framework et Bibliothèques Principales
======================================

- **Django** (version 5.1) : Framework web pour le développement de l'application.
- **Gunicorn** (version 23.0.0) : Serveur WSGI pour servir l'application Django en production.
- **Whitenoise** (version 6.7.0) : Pour servir les fichiers statiques dans Django en production.

Outils de Développement
=======================

- **Black** (version 24.8.0) : Outil de formatage automatique du code Python.
- **Flake8** (version 7.1.1) : Outil pour le linting du code Python.
- **Coverage** (version 7.6.1) : Outil pour mesurer la couverture de code des tests.

Outils de Test
==============

- **pytest** (version 8.3.2) : Framework de test pour Python.
- **pytest-django** (version 4.8.0) : Extensions pour tester des applications Django avec pytest.
- **pytest-cov** (version 5.0.0) : Plugin pour mesurer la couverture des tests avec pytest.
- **factory_boy** (version 3.3.1) : Bibliothèque pour créer des objets de test.

Gestion des Dépendances et Environnements
=========================================

- **django-environ** (version 0.11.2) : Outil pour gérer les paramètres de configuration à partir des variables d'environnement.

Surveillance et Suivi des Erreurs
=================================

- **sentry-sdk** (version 2.13.0) : Intégration avec Sentry pour le suivi des erreurs et la surveillance.
