# Generated by Django 4.2.5 on 2023-11-27 00:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cs3240', '0008_place_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='delete',
            new_name='delete_place',
        ),
    ]
