# Generated by Django 4.2.1 on 2023-05-29 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_carrito_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='persona',
            old_name='genero',
            new_name='sexo',
        ),
    ]
