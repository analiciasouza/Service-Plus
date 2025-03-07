# Generated by Django 5.1.6 on 2025-03-07 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='categorias/')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('professional', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='servicos/')),
                ('categoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='home.categoria')),
            ],
        ),
    ]
