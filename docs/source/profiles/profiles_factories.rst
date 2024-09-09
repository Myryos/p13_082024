=============================
Profiles Factories
=============================

Ce module définit des classes de factory pour générer des instances des modèles
`User` et `Profile` à des fins de test. Les factories sont utilisées pour créer
des objets de manière simple et cohérente dans les tests unitaires, en générant
des données réalistes sans avoir à les créer manuellement.

Classes :
- `UserFactory` : Génère des instances du modèle `User`.
- `ProfileFactory` : Génère des instances du modèle `Profile`,
avec un utilisateur associé généré par `UserFactory`.

.. autoclass:: profiles.factories.UserFactory
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: profiles.factories.ProfileFactory
   :members:
   :undoc-members:
   :show-inheritance:
