# Generated by Django 2.1.7 on 2019-04-03 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0007_auto_20190403_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='newoccupation',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='info',
            name='newsex',
            field=models.TextField(),
        ),
    ]
