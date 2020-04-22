# Generated by Django 3.0.5 on 2020-04-20 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('seccondname', models.CharField(max_length=30)),
                ('studentID', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(max_length=30)),
                ('phoneNo', models.CharField(max_length=30)),
            ],
        ),
    ]
