=============================
Lettings Factories
=============================

Ce module définit des classes de factory pour générer des instances des modèles
`Address` et `Letting` à des fins de test. Les factories sont utilisées pour créer
des objets de manière simple et cohérente dans les tests unitaires, en générant
des données réalistes sans avoir à les créer manuellement.

Classes :
- `AddressFactory` : Génère des instances du modèle `Address`.
- `LettingFactory` : Génère des instances du modèle `Letting`,
avec une adresse associée générée par `AddressFactory`.

.. autoclass:: lettings.factories.AddressFactory
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: lettings.factories.LettingFactory
   :members:
   :undoc-members:
   :show-inheritance:
