# Generated by Django 5.0.7 on 2024-09-23 16:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Estadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('localizacao', models.CharField(max_length=255)),
                ('capacidade', models.IntegerField()),
                ('data_construcao', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Estadios',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=255)),
                ('resposta_correta', models.CharField(max_length=255)),
                ('alternativas', models.TextField(help_text='Insira as alternativas separadas por vírgula')),
            ],
            options={
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField()),
                ('comentario', models.TextField(blank=True, null=True)),
                ('data_avaliacao', models.DateTimeField(auto_now_add=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Avaliacoes',
            },
        ),
        migrations.CreateModel(
            name='Ingresso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_jogo', models.DateField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('quantidade_disponivel', models.IntegerField()),
                ('estadio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estadio')),
            ],
            options={
                'verbose_name_plural': 'Ingressos',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('estadio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.estadio')),
            ],
            options={
                'verbose_name_plural': 'Times',
            },
        ),
        migrations.CreateModel(
            name='UsuarioPerfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]