# Generated by Django 4.0.5 on 2022-11-16 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProTracker', '0005_remove_matchinfo_player_matchinfo_match_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchinfo',
            name='match_patch',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
