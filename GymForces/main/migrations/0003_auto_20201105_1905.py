# Generated by Django 3.1.2 on 2020-11-05 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_registro_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(null=True, upload_to='registro')),
            ],
        ),
        migrations.RemoveField(
            model_name='registro',
            name='imagen',
        ),
    ]
