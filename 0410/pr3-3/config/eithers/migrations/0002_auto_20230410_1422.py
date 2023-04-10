# Generated by Django 3.2.18 on 2023-04-10 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eithers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pick', models.BooleanField()),
                ('content', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('issue_a', models.CharField(max_length=100)),
                ('issue_b', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Either',
        ),
        migrations.AddField(
            model_name='comment',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='eithers.question'),
        ),
    ]