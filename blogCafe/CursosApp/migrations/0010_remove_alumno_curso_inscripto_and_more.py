# Generated by Django 4.2.5 on 2023-10-16 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CursosApp', '0009_alter_comentario_options_comentario_fechacomentario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='curso_inscripto',
        ),
        migrations.AddField(
            model_name='alumno',
            name='cursos_inscriptos',
            field=models.ManyToManyField(blank=True, to='CursosApp.curso'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nacimiento',
            field=models.DateField(null=True),
        ),
    ]
