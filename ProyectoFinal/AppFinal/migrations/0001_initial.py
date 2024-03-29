# Generated by Django 4.0.5 on 2022-08-12 11:58

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
            name='Futbol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_equipo', models.CharField(max_length=40)),
                ('integrantes', models.IntegerField()),
                ('email_representante', models.EmailField(max_length=254)),
                ('telefono_contacto', models.CharField(max_length=40)),
                ('id_torneo', models.IntegerField()),
                ('fecha_de_registro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TenisSingle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_participante', models.CharField(max_length=40)),
                ('email_tenista', models.EmailField(max_length=254)),
                ('telefono_contacto', models.CharField(max_length=40)),
                ('id_torneo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Volley',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_equipo', models.CharField(max_length=40)),
                ('integrantes', models.IntegerField()),
                ('email_representante', models.EmailField(max_length=254)),
                ('telefono_contacto', models.CharField(max_length=40)),
                ('id_torneo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(default='avatares/11.jpg', upload_to='avatares')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
