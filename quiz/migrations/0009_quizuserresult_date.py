# Generated by Django 3.0.2 on 2020-01-24 09:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_quizuserresult_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizuserresult',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]