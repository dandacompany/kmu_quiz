# Generated by Django 5.1.1 on 2024-09-12 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_delete_useranswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='dislikes',
            field=models.IntegerField(default=0, verbose_name='싫어요'),
        ),
    ]
