# Generated by Django 5.1.2 on 2024-12-01 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_notification'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-created_at']},
        ),
    ]
