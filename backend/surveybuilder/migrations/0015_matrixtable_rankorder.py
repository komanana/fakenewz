# Generated by Django 3.2.7 on 2022-09-19 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0014_socialpostquestion_articleuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='RankOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=None)),
                ('title', models.CharField(blank=True, default='', max_length=5000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.multichoicequestion')),
            ],
        ),
        migrations.CreateModel(
            name='MatrixTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=None)),
                ('title', models.CharField(blank=True, default='', max_length=5000)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.multichoicequestion')),
            ],
        ),
    ]
