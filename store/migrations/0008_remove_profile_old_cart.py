# Generated by Django 5.1.2 on 2024-11-26 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_profile_old_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='old_cart',
        ),
    ]
