# Generated by Django 4.2.5 on 2023-10-07 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
    ]
