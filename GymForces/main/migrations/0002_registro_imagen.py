# Generated by Django 3.1.2 on 2020-11-05 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='imagen',
            field=models.ImageField(null=True, upload_to='registro'),
        ),
    ]
