# Generated by Django 5.1.2 on 2024-10-21 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_remove_estadio_preferencia_estadio_imagem_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avaliacao',
            name='estrelas',
        ),
    ]