# Generated by Django 2.0.8 on 2019-03-22 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0003_auto_20190322_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratings',
            name='movie_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='film.Movies'),
        ),
    ]