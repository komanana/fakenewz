# Generated by Django 3.2.7 on 2022-05-06 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveytaker', '0009_merge_20220502_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='response',
            name='completion_rate',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='response',
            name='uuid',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='responseblock',
            name='uuid',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='responsequestionanswer',
            name='uuid',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
