# Generated by Django 3.2.7 on 2022-03-31 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0002_auto_20220329_0342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buttonquestion',
            name='goToEnd',
        ),
        migrations.RemoveField(
            model_name='buttonrowquestion',
            name='goToEnd',
        ),
        migrations.AddField(
            model_name='buttonquestion',
            name='jumpBlockId',
            field=models.IntegerField(default=0),
        ),
    ]
