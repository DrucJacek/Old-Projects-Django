# Generated by Django 4.2.11 on 2024-03-22 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokoje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=255)),
                ('cena', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'pokoje',
            },
        ),
        migrations.CreateModel(
            name='Rezerwacje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liczba_dni', models.IntegerField()),
                ('sezon', models.CharField(max_length=255)),
                ('id_pokoju', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokojeapp.pokoje')),
            ],
            options={
                'verbose_name_plural': 'rezerwacje',
            },
        ),
    ]
