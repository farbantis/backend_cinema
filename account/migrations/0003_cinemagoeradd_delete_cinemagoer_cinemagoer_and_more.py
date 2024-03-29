# Generated by Django 4.1.7 on 2023-02-23 16:04

import account.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_cinemaadmin_options_alter_cinemagoer_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='CinemaGoerAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, null=True, upload_to=account.validators.upload_path_and_rename, validators=[django.core.validators.validate_image_file_extension, account.validators.validate_file_size])),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE'), ('N', '-')], default='N', max_length=15)),
                ('status', models.CharField(choices=[('BRONZE', 'BRONZE'), ('SILVER', 'SILVER'), ('GOLD', 'GOLD'), ('PLATINUM', 'PLATINUM')], default='BRONZE', max_length=15)),
                ('bonus', models.IntegerField(default=0)),
                ('amount_of_purchase', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='CinemaGoer',
        ),
        migrations.CreateModel(
            name='CinemaGoer',
            fields=[
            ],
            options={
                'verbose_name': 'CinemaGoer',
                'verbose_name_plural': 'CinemaGoers',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('account.user',),
        ),
        migrations.AddField(
            model_name='cinemagoeradd',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.cinemagoer'),
        ),
    ]
