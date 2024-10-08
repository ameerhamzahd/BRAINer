# Generated by Django 5.0.3 on 2024-05-10 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Brainer', '0011_alter_userprofile_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='condition',
            field=models.CharField(blank=True, choices=[('Worst', 'Worst'), ('Bad', 'Bad'), ('Medium', 'Medium'), ('Good', 'Good'), ('Excellent', 'Excellent')], max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='percentage',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
