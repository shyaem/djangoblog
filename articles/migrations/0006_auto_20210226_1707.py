# Generated by Django 3.1.7 on 2021-02-26 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20210226_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=models.TextField(max_length=1000),
        ),
    ]
