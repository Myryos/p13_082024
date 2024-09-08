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

- **ASGIRef** (version 3.8.1) : Fournit des outils pour le support ASGI.
- **Black** (version 24.8.0) : Outil de formatage automatique du code Python.
- **Flake8** (version 7.1.1) : Outil pour le linting du code Python.
- **Mypy-Extensions** (version 1.0.0) : Extensions pour Mypy, un vérificateur de types statiques pour Python.
- **Coverage** (version 7.6.1) : Outil pour mesurer la couverture de code des tests.

Outils de Test
==============

- **pytest** (version 8.3.2) : Framework de test pour Python.
- **pytest-django** (version 4.8.0) : Extensions pour tester des applications Django avec pytest.
- **pytest-cov** (version 5.0.0) : Plugin pour mesurer la couverture des tests avec pytest.
- **pytest-mock** (version 3.14.0) : Plugin pour intégrer le mocking avec pytest.
- **factory_boy** (version 3.3.1) : Bibliothèque pour créer des objets de test.

Gestion des Dépendances et Environnements
=========================================

- **django-environ** (version 0.11.2) : Outil pour gérer les paramètres de configuration à partir des variables d'environnement.
- **dj-database-url** (version 2.2.0) : Utilisé pour configurer les bases de données via une URL.
- **psycopg2-binary** (version 2.9.9) : Connecteur PostgreSQL pour Django.

Autres Dépendances
==================

- **sentry-sdk** (version 2.13.0) : Intégration avec Sentry pour le suivi des erreurs et la surveillance.
- **Faker** (version 28.1.0) : Bibliothèque pour générer des données factices.
- **certifi** (version 2024.7.4) : Fournit des certificats CA pour des connexions sécurisées.
- **click** (version 8.1.7) : Utilisé pour la gestion des commandes en ligne de commande.
- **entrypoints** (version 0.4) : Outil pour les points d'entrée dans les paquets Python.
- **exceptiongroup** (version 1.2.2) : Gère les groupes d'exceptions.
- **platformdirs** (version 4.2.2) : Fournit des répertoires spécifiques à la plateforme pour les applications Python.
- **packaging** (version 24.1) : Utilisé pour la gestion des versions et des dépendances.

Dépendances de Test et Développement
====================================

- **pycodestyle** (version 2.12.1) : Outil de vérification de la conformité du code aux normes de style Python.
- **pyflakes** (version 3.2.0) : Analyseur statique de code pour Python.
- **typing_extensions** (version 4.12.2) : Extensions pour le système de types de Python.

Ces outils et bibliothèques sont essentiels pour le développement, les tests, le déploiement et la maintenance de l'application. Assurez-vous de respecter les versions spécifiées pour garantir la compatibilité et la stabilité du projet.
