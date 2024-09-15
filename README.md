## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/Myryos/p13_082024.git`

#### Créer l'environnement virtuel

- `cd /path/to/p13_082024`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/p13_082024`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/p13_082024`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/p13_082024`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/p13_082024`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

### Prérequis
- Un compte sur un service de déploiement (J'ai personnellement utilisé Render)
- Un accès à un Docker Hub ou un autre registre Docker pour stocker votre image.
- Une clé API pour votre service de déploiement
- Docker installé localement pour construire votre image et tester localement le container.
### Étapes de déploiement
1. Création de l'image Docker
Avant de déployer, il est nécessaire de créer une image Docker de l'application. Le Dockerfile fourni dans le projet configure la création de l'image pour Django et Gunicorn.
- Assurez-vous que votre projet est à jour en local.
- Dans le répertoire racine du projet, exécutez la commande suivante pour construire l'image Docker : 
``` docker build -t <votre_nom_d_utilisateur_dockerhub>/oc-lettings:latest .```
  - Remplacez <votre_nom_d_utilisateur_dockerhub> par votre nom d'utilisateur Docker Hub.
  - L'image sera créée avec le tag latest, que vous pouvez changer en fonction de votre stratégie de versionnage (comme l'usage d'un hash de commit par exemple).
2. Push l'image vers Docker Hub
Pour que le service Render (ou un autre service de déploiement) puisse accéder à l'image Docker, vous devez la pousser vers un registre Docker, comme Docker Hub.
- Connectez-vous à Docker Hub depuis votre terminal :
``` docker login ```
- Poussez l'image vers Docker Hub :
``` docker push <votre_nom_d_utilisateur_dockerhub>/oc-lettings:latest ```
3.  Déployer sur Render
Si vous utilisez Render, suivez les étapes ci-dessous pour déployer votre image.

 1. Création du service Render : Allez sur le tableau de bord Render et créez un nouveau service en sélectionnant l'option "Web Service" et en choisissant "Docker" comme environnement.
 2. Configurer le déploiement :
  - Dans le champ Docker Registry, fournissez l'URL de votre image Docker Hub, par exemple :
    ``` docker.io/<votre_nom_d_utilisateur_dockerhub>/oc-lettings:latest ```
  - Configurez les variables d'environnement nécessaires (comme DJANGO_SECRET_KEY, DATABASE_URL, etc.).
 3. Déploiement automatique :  Si vous avez configuré un pipeline CI/CD, vous pouvez automatiser le processus pour qu'à chaque push vers une branche principale (par exemple master), une nouvelle image Docker soit créée et déployée automatiquement. Utilisez la commande curl suivante pour déclencher un déploiement via l'API de Render :
    ``` 
    curl -X POST \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer ${{ secrets.RENDER_API_KEY }}" \
     https://api.render.com/v1/services/<votre-service-id>/deploys

     ```
     Vous pouvez également configurer votre pipeline pour créer une nouvelle image Docker et la pousser vers Docker Hub à chaque build.
 4. Vérification
  - Après le déploiement, accédez à l'URL fournie par Render pour vérifier que l'application est fonctionnelle.
  - Si des fichiers statiques ne se chargent pas correctement, vérifiez que WhiteNoise est configuré pour servir ces fichiers dans settings.py (voir la section WhiteNoise dans ce fichier README).
  - Vous pouvez accéder à l'interface d'administration via l'URL /admin en utilisant les identifiants fournis précédemment.
 5. Mises à jours
  Pour déployer une nouvelle version :
  - Créez une nouvelle image Docker en répétant les étapes de build et de push Docker.
  - Déclenchez un nouveau déploiement dans Render, ou laissez le pipeline CI/CD faire automatiquement le déploiement.
### Remarques supplémentaires

  - Assurez-vous que le fichier requirements.txt est bien mis à jour si des dépendances ont changé avant chaque build Docker.
  - Si vous utilisez une base de données autre que SQLite (comme PostgreSQL), configurez correctement les variables d'environnement dans Render (notamment DATABASE_URL).
