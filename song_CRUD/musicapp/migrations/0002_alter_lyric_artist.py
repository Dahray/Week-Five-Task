# Generated by Django 4.1.2 on 2022-10-29 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("musicapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lyric",
            name="artist",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.RESTRICT, to="musicapp.artist"
            ),
        ),
    ]
