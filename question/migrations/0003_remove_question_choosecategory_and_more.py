# Generated by Django 4.0.5 on 2022-06-27 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question', '0002_question_choosecategory_question_choosetopic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='chooseCategory',
        ),
        migrations.RemoveField(
            model_name='question',
            name='chooseTopic',
        ),
    ]