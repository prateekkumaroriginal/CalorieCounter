# Generated by Django 4.2.7 on 2023-11-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='weight',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]