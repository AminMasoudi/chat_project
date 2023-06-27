# Generated by Django 4.2.2 on 2023-06-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_remove_usersprofile_rooms"),
        ("chaty", "0004_alter_massage_content"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="massage",
            options={"ordering": ["time"]},
        ),
        migrations.AddField(
            model_name="room",
            name="member",
            field=models.ManyToManyField(
                blank=True, related_name="rooms", to="user.usersprofile"
            ),
        ),
    ]