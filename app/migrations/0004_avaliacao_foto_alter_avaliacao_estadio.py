# Generated by Django 5.1.1 on 2024-10-01 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_estadio_descricao_alter_estadio_nome_avaliacao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='avaliacao',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='avaliacoes/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='avaliacao',
            name='estadio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estadio', verbose_name='Estádio'),
        ),
    ]
