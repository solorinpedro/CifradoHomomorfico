# Generated by Django 4.2.8 on 2024-01-02 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(blank=True, null=True)),
                ('apellido', models.TextField(blank=True, null=True)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('cedula', models.TextField(blank=True, null=True)),
            ],
        ),
    ]