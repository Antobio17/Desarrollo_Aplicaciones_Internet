# Generated by Django 3.1.4 on 2020-12-10 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mi_aplicacion', '0005_auto_20201210_1727'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ejemplar',
            options={},
        ),
        migrations.RemoveField(
            model_name='ejemplar',
            name='estado',
        ),
    ]
