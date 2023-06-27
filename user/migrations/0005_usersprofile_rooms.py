# Generated by Django 4.2.2 on 2023-06-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chaty", "0006_remove_room_member"),
        ("user", "0004_remove_usersprofile_rooms"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersprofile",
            name="rooms",
            field=models.ManyToManyField(related_name="member", to="chaty.room"),
        ),
    ]