# Generated by Django 3.1.1 on 2020-09-15 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_profile_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='job',
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, default='my location default', max_length=120, null=True),
        ),
    ]
