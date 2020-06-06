# Generated by Django 3.0.6 on 2020-06-06 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=200)),
                ('class_id', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=60)),
                ('unit_code', models.CharField(max_length=60)),
                ('tutor_contact', models.CharField(max_length=10)),
                ('classroo_id', models.ManyToManyField(to='portal.Classroom')),
                ('tutor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_createdby', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_title', models.FileField(null=True, upload_to='notes')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.Unit')),
            ],
        ),
    ]
