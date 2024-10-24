# Generated by Django 5.0.7 on 2024-10-18 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_time_brasao_alter_time_cidade_alter_time_estadio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome de usuário')),
                ('email', models.EmailField(max_length=100, verbose_name='Email do usuário')),
                ('senha', models.CharField(max_length=30, verbose_name='Senha do usuário')),
            ],
            options={
                'verbose_name': 'Ingresso',
                'verbose_name_plural': 'Ingressos',
            },
        ),
    ]
