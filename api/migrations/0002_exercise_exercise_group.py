# Generated by Django 3.2.7 on 2021-09-30 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='exercise_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.exercisegroup'),
        ),
    ]
