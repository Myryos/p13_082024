from django.db import migrations


def transfer_data(apps, schema_editor):
    """
    Transfert les données des anciennes tables vers les nouvelles tables.
    """
    # Obtenez les anciens et nouveaux modèles
    OldAddress = apps.get_model("oc_lettings_site", "Address")
    OldLetting = apps.get_model("oc_lettings_site", "Letting")
    NewAddress = apps.get_model("lettings", "Address")
    NewLetting = apps.get_model("lettings", "Letting")

    # Transférez les données d'Address
    for old_address in OldAddress.objects.all():
        NewAddress.objects.create(
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )

    # Transférez les données de Letting
    for old_letting in OldLetting.objects.all():
        # Trouvez l'adresse correspondante dans la nouvelle table
        address = NewAddress.objects.get(
            number=old_letting.address.number,
            street=old_letting.address.street,
            city=old_letting.address.city,
            state=old_letting.address.state,
            zip_code=old_letting.address.zip_code,
            country_iso_code=old_letting.address.country_iso_code,
        )
        NewLetting.objects.create(title=old_letting.title, address=address)


class Migration(migrations.Migration):

    dependencies = [
        (
            "lettings",
            "0001_initial",
        ),
        (
            "oc_lettings_site",
            "0001_initial",
        ),  # Assurez-vous que cette dépendance correspond à votre première migration initiale
    ]

    operations = [
        migrations.RunPython(transfer_data),
    ]
