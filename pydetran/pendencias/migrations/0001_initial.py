# Generated by Django 4.2.6 on 2023-10-13 03:00

from django.db import migrations, models
import pendencias.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pendencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pessoa', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, validators=[pendencias.models.validate_cpf])),
                ('codigo_pa', models.CharField(max_length=10, unique=True)),
                ('descricao', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
