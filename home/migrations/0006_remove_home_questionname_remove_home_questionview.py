# Generated by Django 4.0.5 on 2022-06-27 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_delete_question_home_questionname_home_questionview'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='questionName',
        ),
        migrations.RemoveField(
            model_name='home',
            name='questionView',
        ),
    ]
