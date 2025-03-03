# Generated by Django 3.1.4 on 2020-12-10 16:20

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0003_auto_20201210_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='isbn',
            field=models.CharField(help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, null=True, verbose_name='ISBN'),
        ),
        migrations.AddField(
            model_name='libro',
            name='resumen',
            field=models.TextField(help_text='Breve resumen del libro', max_length=1000, null=True),
        ),
        migrations.CreateModel(
            name='Ejemplar',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID único para el ejemplar del libro físico', primary_key=True, serialize=False)),
                ('devolucion', models.DateField(blank=True, null=True)),
                ('estado', models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Disponibilidad del libro', max_length=1)),
                ('libro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mi_aplicacion.libro')),
            ],
            options={
                'ordering': ['devolucion'],
            },
        ),
        migrations.AddField(
            model_name='prestamo',
            name='ejemplar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mi_aplicacion.ejemplar'),
        ),
    ]
