# Generated by Django 3.0.6 on 2020-06-06 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notes',
            old_name='note_title',
            new_name='note',
        ),
    ]
