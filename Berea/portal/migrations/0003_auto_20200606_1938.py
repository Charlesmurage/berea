# Generated by Django 3.0.6 on 2020-06-06 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20200606_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='note',
            new_name='note_title',
        ),
    ]
