# Generated by Django 5.1.3 on 2024-12-16 00:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consultations', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompteRendu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField(default='')),
                ('resultat', models.TextField()),
                ('fichier_upload', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Examen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_examen', models.CharField(max_length=100)),
                ('compte_rendu', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='examinations.compterendu')),
                ('consultation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultations.consultation')),
                ('laborantin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.laboratin')),
                ('radiologue', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.radiologue')),
            ],
        ),
    ]
