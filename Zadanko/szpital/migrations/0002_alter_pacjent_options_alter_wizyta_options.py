# Generated by Django 4.2.6 on 2023-10-06 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('szpital', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pacjent',
            options={'verbose_name_plural': 'Pacjent'},
        ),
        migrations.AlterModelOptions(
            name='wizyta',
            options={'verbose_name_plural': 'Wizyta'},
        ),
    ]
