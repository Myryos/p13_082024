=============================
Lettings Models
=============================

Ce module contient les modèles de données pour l'application de gestion des annonces
de location. Il définit les modèles suivants :

- :class:`Address` : Représente une adresse physique, incluant des détails comme le numéro
  de rue, le nom de la rue, la ville, l'état, le code postal, et le code ISO du pays.
- :class:`Letting` : Représente une annonce de location, associée à une adresse et incluant
  un titre pour l'annonce.

.. autoclass:: lettings.models.Address
   :members:
   :undoc-members:
   :show-inheritance:

.. autoclass:: lettings.models.Letting
   :members:
   :undoc-members:
   :show-inheritance:
