# Generated by Django 4.2.3 on 2023-10-13 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CursosApp', '0003_rename_curso_curso_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(null=True, upload_to='cursos'),
        ),
    ]
