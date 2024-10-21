# Generated by Django 5.1.1 on 2024-10-01 11:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_avaliacao_foto_alter_avaliacao_estadio'),
    ]

    operations = [
        migrations.AddField(
            model_name='time',
            name='brasao',
            field=models.ImageField(blank=True, help_text='Carregue o brasão do time', null=True, upload_to='brasoes/'),
        ),
        migrations.AlterField(
            model_name='time',
            name='cidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade'),
        ),
        migrations.AlterField(
            model_name='time',
            name='estadio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.estadio'),
        ),
        migrations.AlterField(
            model_name='time',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
