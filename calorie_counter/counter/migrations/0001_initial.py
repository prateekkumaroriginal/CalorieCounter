# Generated by Django 4.2.7 on 2023-11-25 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('carbs', models.DecimalField(decimal_places=1, max_digits=10)),
                ('protein', models.DecimalField(decimal_places=1, max_digits=10)),
                ('fats', models.DecimalField(decimal_places=1, max_digits=10)),
                ('calories', models.IntegerField()),
            ],
        ),
    ]
