# Generated by Django 2.1.7 on 2019-04-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0005_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='info',
            name='occupation',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='sex',
            field=models.CharField(max_length=255, null=True),
        ),
    ]