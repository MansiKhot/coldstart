# Generated by Django 2.1.7 on 2019-04-03 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0008_auto_20190403_1953'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='newage',
        ),
        migrations.RemoveField(
            model_name='info',
            name='newoccupation',
        ),
        migrations.RemoveField(
            model_name='info',
            name='newsex',
        ),
    ]
