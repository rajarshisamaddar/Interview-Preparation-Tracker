# Generated by Django 4.0.3 on 2022-06-28 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic_cIdentifier',
            field=models.CharField(default='', max_length=64, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topic',
            name='topic_tIdentifier',
            field=models.CharField(default='', max_length=64, unique=True),
            preserve_default=False,
        ),
    ]
