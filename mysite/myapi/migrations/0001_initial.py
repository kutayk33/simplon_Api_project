# Generated by Django 3.2.4 on 2021-06-04 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departement',
            fields=[
                ('Intitule', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Etage', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Prenom', models.CharField(max_length=10)),
                ('Nom', models.CharField(max_length=10)),
                ('Age', models.SmallIntegerField(default=30)),
                ('Ville', models.CharField(max_length=100)),
                ('Poste', models.CharField(max_length=100)),
                ('Salaire', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapi.departement')),
            ],
        ),
    ]
