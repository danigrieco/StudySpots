# Generated by Django 4.2.5 on 2023-11-11 19:11

from django.db import migrations, models
import django_google_maps.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cs3240', '0002_alter_place_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='address',
            field=django_google_maps.fields.AddressField(default='NULL', max_length=200),
        ),
        migrations.AlterField(
            model_name='place',
            name='details',
            field=models.CharField(default='NULL', max_length=700),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(default='NULL', max_length=200),
        ),
    ]