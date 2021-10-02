# Generated by Django 3.2.7 on 2021-10-01 22:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211001_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='question',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='title',
        ),
        migrations.AlterField(
            model_name='answer',
            name='answered',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='api.alternative', verbose_name='Escolha do usuário'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='exercise_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='exercises', to='api.exercisegroup', verbose_name='Lista de Exercício'),
        ),
        migrations.AlterUniqueTogether(
            name='alternative',
            unique_together={('letter', 'exercise')},
        ),
        migrations.AlterUniqueTogether(
            name='answer',
            unique_together={('exercise', 'answered')},
        ),
    ]
