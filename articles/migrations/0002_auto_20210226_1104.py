# Generated by Django 3.1.7 on 2021-02-26 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='phone',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
