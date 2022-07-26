# Generated by Django 3.1.3 on 2021-11-18 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gstock', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiaires',
            name='Carte_donnee',
            field=models.CharField(choices=[('Non', 'Non'), ('Oui', 'Oui')], default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='beneficiaires',
            name='Mot_mairie',
            field=models.CharField(choices=[('Non', 'Non'), ('Oui', 'Oui')], default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='beneficiaires',
            name='Nb_parts',
            field=models.CharField(choices=[('15-25 ans', '15-25 ans'), ('25-64 ans', '25-64 ans'), ('Plus de 65 ans', 'Plus de 65 ans'), ('4-14 ans', '4-14 ans'), ('0-3 ans', '0-3 ans')], default='1', max_length=200),
        ),
        migrations.AlterField(
            model_name='beneficiaires',
            name='Telephone',
            field=models.FloatField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='categories',
            name='Unite',
            field=models.CharField(choices=[('Kilo', 'Kilo'), ('Litre', 'Litre'), ('Unité', 'Unité')], default='2', max_length=200),
        ),
    ]
