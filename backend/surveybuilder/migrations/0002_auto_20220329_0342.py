# Generated by Django 3.2.7 on 2022-03-28 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RandomSections',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('display', models.IntegerField(default=1)),
                ('startWith', models.IntegerField(default=None)),
                ('endWith', models.IntegerField(default=None)),
                ('index', models.IntegerField(default=None)),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.survey')),
            ],
        ),
        migrations.RemoveField(
            model_name='block',
            name='randomiser',
        ),
        migrations.DeleteModel(
            name='Randomiser',
        ),
    ]
