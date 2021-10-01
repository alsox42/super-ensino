# Generated by Django 3.2.7 on 2021-10-01 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20211001_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='sub_title',
        ),
        migrations.AddField(
            model_name='exercise',
            name='question',
            field=models.CharField(default='ww', max_length=100, verbose_name='Pergunta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='answered',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.alternative', verbose_name='Escolha do usuário'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='exercise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.exercise', verbose_name='Exercicio'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
        migrations.AlterField(
            model_name='exercisegroup',
            name='text',
            field=models.CharField(max_length=150, verbose_name='Nome da Lista?'),
        ),
        migrations.AlterField(
            model_name='exercisegroup',
            name='the_amount',
            field=models.IntegerField(default=0, verbose_name='Quant. de Exerc.'),
        ),
    ]