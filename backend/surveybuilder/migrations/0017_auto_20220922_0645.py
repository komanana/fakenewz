# Generated by Django 3.2.7 on 2022-09-22 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0016_matrixtablequestion_rankorderquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='matrixtablequestion',
            name='columnConfig',
            field=models.TextField(blank=True, default='[]', max_length=5000),
        ),
        migrations.AlterField(
            model_name='matrixtable',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.matrixtablequestion'),
        ),
        migrations.AlterField(
            model_name='rankorder',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.rankorderquestion'),
        ),
    ]
