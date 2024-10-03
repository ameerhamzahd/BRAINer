# Generated by Django 5.0.3 on 2024-05-17 15:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brainer', '0020_userprofile_braiqui_de_avareg_last_5_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ReactionTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_time', models.FloatField(blank=True, null=True)),
                ('last_ten_games_average', models.FloatField(blank=True, null=True)),
                ('last_game_average', models.FloatField(blank=True, null=True)),
                ('overall_average', models.FloatField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
