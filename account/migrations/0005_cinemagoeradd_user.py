# Generated by Django 4.1.7 on 2023-02-23 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_cinemagoeradd_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinemagoeradd',
            name='user',
            field=models.OneToOneField(default=12, on_delete=django.db.models.deletion.CASCADE, to='account.cinemagoer'),
        ),
    ]
