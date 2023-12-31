# Generated by Django 4.2.5 on 2023-10-16 02:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CursosApp', '0008_curso_descripcion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['-fechaComentario']},
        ),
        migrations.AddField(
            model_name='comentario',
            name='fechaComentario',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='comentario',
            name='mensaje',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='comentario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='CursosApp.curso'),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='nombre',
            field=models.CharField(max_length=40),
        ),
    ]
