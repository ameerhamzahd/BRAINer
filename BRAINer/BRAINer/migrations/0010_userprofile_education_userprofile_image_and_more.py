# Generated by Django 5.0.3 on 2024-05-10 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brainer', '0009_remove_userprofile_condition_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='education',
            field=models.CharField(blank=True, choices=[('High School', 'High School'), ('Bachelor', 'Bachelor'), ('Master', 'Master'), ('PhD', 'PhD'), ('Other', 'Other')], max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='user_profile_images/'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='job',
            field=models.CharField(blank=True, choices=[('Engineer', 'Engineer'), ('Doctor', 'Doctor'), ('Teacher', 'Teacher'), ('Other', 'Other')], max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='language',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
