# Generated by Django 3.2.7 on 2022-05-02 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveybuilder', '0007_auto_20220502_0417'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='if_capture_gaze',
            field=models.BooleanField(default=True),
        ),
    ]