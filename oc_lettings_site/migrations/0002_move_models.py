from django.db import migrations


def move_models(apps, schema_editor):
    OldAddress = apps.get_model("oc_lettings_site", "Address")
    OldLetting = apps.get_model("oc_lettings_site", "Letting")
    OldProfile = apps.get_model("oc_lettings_site", "Profile")

    NewAddress = apps.get_model("lettings", "Address")
    NewLetting = apps.get_model("lettings", "Letting")
    NewProfile = apps.get_model("profiles", "Profile")

    for old_address in OldAddress.objects.all():
        new_address = NewAddress(
            id=old_address.id,
            number=old_address.number,
            street=old_address.street,
            city=old_address.city,
            state=old_address.state,
            zip_code=old_address.zip_code,
            country_iso_code=old_address.country_iso_code,
        )
        new_address.save()

    for old_letting in OldLetting.objects.all():
        new_letting = NewLetting(
            id=old_letting.id,
            title=old_letting.title,
            address_id=old_letting.address_id,
        )
        new_letting.save()

    for old_profile in OldProfile.objects.all():
        new_profile = NewProfile(
            id=old_profile.id,
            user_id=old_profile.user_id,
            favorite_city=old_profile.favorite_city,
        )
        new_profile.save()


class Migration(migrations.Migration):
    dependencies = [
        ("lettings", "0001_initial"),
        ("profiles", "0001_initial"),
        (
            "oc_lettings_site",
            "0001_initial",
        ),  # Remplacez par le nom de la dernière migration
    ]

    operations = [
        migrations.RunPython(move_models),
    ]
