=========================
Instructions d'Installation
=========================

Pour installer et configurer le projet Django, suivez les étapes ci-dessous :

Prérequis
=========

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

macOS / Linux
=============

1. **Cloner le repository** :

   .. code-block:: bash

      cd /path/to/put/project/in
      git clone https://github.com/Myryos/p13_082024.git

2. **Créer l'environnement virtuel** :

   .. code-block:: bash

      cd /path/to/Python-OC-Lettings-FR
      python -m venv venv
      apt-get install python3-venv  # Si nécessaire sur Ubuntu
      source venv/bin/activate
      which python
      python --version
      which pip

3. **Installer les dépendances** :

   .. code-block:: bash

      pip install --requirement requirements.txt

4. **Configurer et exécuter le site** :

   .. code-block:: bash

      python manage.py runserver

   Accédez à http://localhost:8000 pour vérifier que le site fonctionne.

Windows
=======

1. **Activer l'environnement virtuel** :

   .. code-block:: bash

      .\venv\Scripts\Activate.ps1

2. Remplacer ``which <my-command>`` par ``(Get-Command <my-command>).Path``.
