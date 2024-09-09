=========================
Structure de la Base de Données
=========================

Le projet **Orange County Lettings** utilise SQLite comme base de données pour le développement local. Voici les instructions pour explorer et interagir avec la base de données.


Instructions pour Explorer la Base de Données
=============================================

Pour explorer la base de données SQLite utilisée dans le projet, suivez ces étapes :

1. **Ouvrir une session shell SQLite** :

   .. code-block:: bash

      sqlite3 oc-lettings-site.sqlite3

2. **Afficher les tables** :

   .. code-block:: sql

      .tables

3. **Afficher les colonnes dans la table des profils** :

   .. code-block:: sql

      pragma table_info(Python-OC-Lettings-FR_profile);

4. **Lancer une requête sur les profils** :

   .. code-block:: sql

      select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';

5. **Quitter** :

   .. code-block:: sql

      .quit

Ces instructions vous permettront d'interagir avec la base de données SQLite et d'explorer les tables et les données stockées.
