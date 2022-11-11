# Generated by Django 4.0.5 on 2022-11-11 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProTracker', '0002_rename_team_id_team_team_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='playeraccount',
            name='account_name',
            field=models.CharField(default='0000000000000000', max_length=16),
        ),
        migrations.AddField(
            model_name='playeraccount',
            name='account_region',
            field=models.CharField(default='0000', max_length=4),
        ),
    ]