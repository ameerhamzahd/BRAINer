# Generated by Django 5.0.3 on 2024-05-10 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brainer', '0007_userprofile_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(max_length=150),
        ),
    ]
