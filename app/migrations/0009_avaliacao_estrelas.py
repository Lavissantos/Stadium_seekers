# Generated by Django 5.1.2 on 2024-10-21 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_usuario_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='estrelas',
            field=models.PositiveIntegerField(default=0, verbose_name='Estrelas'),
        ),
    ]
