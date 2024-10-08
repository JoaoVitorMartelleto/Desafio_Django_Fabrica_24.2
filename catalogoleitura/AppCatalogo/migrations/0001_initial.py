# Generated by Django 5.1 on 2024-08-24 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('data_publi', models.DateField()),
                ('lido', models.BooleanField(default=False)),
                ('nota', models.FloatField(blank=True, null=True)),
                ('comentarios', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppCatalogo.livro')),
            ],
        ),
    ]
