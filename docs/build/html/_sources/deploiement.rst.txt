=========================
Déploiement et Gestion
=========================

Pour déployer l'application, vous pouvez soit suivre un processus manuel, soit utiliser le pipeline CI/CD configuré. Voici les détails pour les deux méthodes.

Pipeline CI/CD
==============

Le pipeline CI/CD automatisé pour le déploiement de **Orange County Lettings** est configuré avec GitHub Actions. Ce pipeline comprend plusieurs étapes, détaillées ci-dessous :

Déclenchement du Pipeline
-------------------------

- Le pipeline se déclenche sur les branches ``master`` et ``QA``.

Étapes du Pipeline
------------------

Build and Test
~~~~~~~~~~~~~~

- **Checkout Code** : Récupère le code source du repository.
- **Set up Python** : Configure l'environnement Python avec la version spécifiée (3.10).
- **Install dependencies** : Installe les dépendances requises via ``requirements.txt``.
- **Flake8 Linting** : Exécute l'outil de linting Flake8 pour vérifier le style du code.
- **Run database migrations** : Exécute les migrations de la base de données.
- **Run test with coverage** : Lance les tests avec couverture de code, échouant si la couverture est inférieure à 80 %.

Containerize
~~~~~~~~~~~~

- **Set up Docker Buildx** : Configure Docker Buildx pour la construction d'images Docker.
- **Log in to Docker Hub** : Authentifie avec Docker Hub à l'aide des secrets de connexion.
- **Build and push Docker image** : Construit et pousse l'image Docker vers Docker Hub avec un tag basé sur le SHA du commit et le tag ``latest``.
- **Run container locally** : Exécute le conteneur Docker localement si le déploiement se fait sur la branche ``master``.

Deploy
~~~~~~

- **Deploy to Render** : Déploie l'application sur Render en utilisant l'API de Render et les secrets de déploiement.

Étapes de Déploiement Manuel
============================

Pour déployer l'application manuellement, suivez ces étapes :

1. **Création de l'image Docker** :

   .. code-block:: bash

      docker build -t <votre_nom_d_utilisateur_dockerhub>/oc-lettings:latest .

2. **Pousser l'image vers Docker Hub** :

   .. code-block:: bash

      docker login
      docker push <votre_nom_d_utilisateur_dockerhub>/oc-lettings:latest

3. **Déployer sur Render** :
   
   - Créez un nouveau service "Web Service" avec Docker sur Render.
   - Configurez le déploiement avec l'URL de votre image Docker Hub.
   - Configurez les variables d'environnement nécessaires (ex. ``DJANGO_SECRET_KEY``, ``DATABASE_URL``).

4. **Vérification** :
   
   - Accédez à l'URL fournie par Render pour vérifier le déploiement.

5. **Mises à jour** :
   
   - Créez une nouvelle image Docker et poussez-la vers Docker Hub.
   - Déclenchez un nouveau déploiement via Render ou via un pipeline CI/CD.
