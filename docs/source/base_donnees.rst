=========================
Structure de la Base de Données
=========================

Le projet **Orange County Lettings** utilise SQLite comme base de données pour le développement local. Voici une description des modèles de données ainsi que des instructions pour explorer et interagir avec la base de données.

### Modèles

#### Address

Le modèle `Address` représente une adresse physique avec les champs suivants :
- **number** (PositiveIntegerField) : Numéro de la rue (valide jusqu'à 9999).
- **street** (CharField) : Nom de la rue (64 caractères max).
- **city** (CharField) : Nom de la ville (64 caractères max).
- **state** (CharField) : État ou province (2 caractères).
- **zip_code** (PositiveIntegerField) : Code postal (max 99999).
- **country_iso_code** (CharField) : Code ISO du pays (3 caractères).

**Méthodes :**
- `__str__()` : Retourne une chaîne représentant l'adresse sous le format "numéro rue".

**Métadonnées :**
- `db_table` : "oc_lettings_site_address"
- `verbose_name_plural` : "Addresses"

#### Letting

Le modèle `Letting` représente une annonce de location avec les attributs suivants :
- **title** (CharField) : Titre de l'annonce (256 caractères max).
- **address** (OneToOneField) : Relation un-à-un avec le modèle `Address`.

**Méthodes :**
- `__str__()` : Retourne le titre de l'annonce.

**Métadonnées :**
- `db_table` : "oc_lettings_site_letting"

#### Profile

Le modèle `Profile` étend le modèle utilisateur de Django avec les champs suivants :
- **user** (OneToOneField) : Relation un-à-un avec le modèle `User`.
- **favorite_city** (CharField) : Ville favorite de l'utilisateur (64 caractères max, optionnel).

**Méthodes :**
- `__str__()` : Retourne le nom d'utilisateur associé au profil.

**Métadonnées :**
- `db_table` : "oc_lettings_site_profile"

### Instructions pour Explorer la Base de Données

Pour explorer la base de données SQLite utilisée dans le projet, suivez ces étapes :

1. **Ouvrir une session shell SQLite** :
   ```bash
   sqlite3 oc-lettings-site.sqlite3
2. **Afficher les tables** :
    ```sql
    .tables
    ```
3. **Afficher les colonnes dans la table des profils** :
    ```sql
    pragma table_info(Python-OC-Lettings-FR_profile);
    ```

4. **Lancer une requête sur les profils ** :
    ```sql
    select user_id, favorite_city from Python-OC-Lettings-FR_profile where favorite_city like 'B%';
    ```
5. **Quitter** :
    ```sql
    .quit
    ```

Ces instructions vous permettront d'interagir avec la base de données SQLite et d'explorer les tables et les données stockées.