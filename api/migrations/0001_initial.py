# Generated by Django 3.2.7 on 2021-09-30 18:41

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
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=50)),
                ('sub_title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Exercicio',
                'verbose_name_plural': 'Exercicios',
                'ordering': ['order_num'],
            },
        ),
        migrations.CreateModel(
            name='ExerciseGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
                ('the_amount', models.IntegerField(default=1)),
            ],
            options={
                'verbose_name': 'Grupo de Exercicio',
                'verbose_name_plural': 'Grupos de Exercicios',
                'ordering': ['text'],
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Resposta',
                'verbose_name_plural': 'Respostas',
                'ordering': ['user', 'exercise'],
            },
        ),
        migrations.CreateModel(
            name='Alternative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150)),
                ('letter', models.CharField(max_length=1)),
                ('is_right', models.BooleanField(default=False)),
                ('exercise', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.exercise')),
            ],
            options={
                'verbose_name': 'Alternativa',
                'verbose_name_plural': 'Alternativas',
                'ordering': ['letter'],
            },
        ),
    ]
