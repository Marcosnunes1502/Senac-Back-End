# Generated by Django 4.1.4 on 2022-12-16 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("primeiro_app", "0003_cliente"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Cliente",
            new_name="Usuario",
        ),
    ]
