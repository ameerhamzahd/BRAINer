# Generated by Django 5.0.3 on 2024-05-10 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brainer', '0008_alter_userprofile_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='overall_success_rate',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
