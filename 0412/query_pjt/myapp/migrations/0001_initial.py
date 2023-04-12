# Generated by Django 3.2.7 on 2023-04-12 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PetSitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firts_name', models.TextField()),
                ('last_name', models.TextField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('pet_sitter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.petsitter')),
            ],
        ),
    ]
