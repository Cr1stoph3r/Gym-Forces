# Generated by Django 3.1.2 on 2020-11-06 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_galeria_deporte'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('deporte_consulta', models.IntegerField(choices=[[0, 'Deporte'], [1, 'Gym'], [2, 'Krav-maga'], [3, 'yoga']])),
                ('mensaje', models.TextField()),
                ('avisos', models.BooleanField()),
            ],
        ),
    ]