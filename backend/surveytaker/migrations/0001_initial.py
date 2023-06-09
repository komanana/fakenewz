# Generated by Django 3.2.7 on 2022-03-23 14:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('surveybuilder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('survey', models.IntegerField()),
                ('create_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('contact_info', models.CharField(max_length=255, null=True)),
                ('answer_json', models.CharField(max_length=5000000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResponseBlock',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.block')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveytaker.response')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseQuestion',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('block', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveytaker.responseblock')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveybuilder.question')),
            ],
        ),
        migrations.CreateModel(
            name='ResponseQuestionAnswer',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, default='', max_length=5000)),
                ('answerText', models.CharField(blank=True, default='', max_length=50000)),
                ('answerDecimal', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveytaker.responsequestion')),
            ],
        ),
    ]
