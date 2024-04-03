# Generated by Django 4.2.11 on 2024-04-03 06:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stanowiska',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=255)),
                ('opis', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Stanowiska',
            },
        ),
        migrations.CreateModel(
            name='Pracownicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=255)),
                ('nazwisko', models.CharField(max_length=255)),
                ('adres', models.CharField(max_length=255)),
                ('miasto', models.CharField(max_length=255)),
                ('czyRodo', models.IntegerField()),
                ('czy_badania', models.IntegerField()),
                ('dataUr', models.DateField()),
                ('stanowiska_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pracoapp.stanowiska')),
            ],
            options={
                'verbose_name_plural': 'Pracownicy',
            },
        ),
    ]