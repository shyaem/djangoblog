# Generated by Django 3.1.7 on 2021-03-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_detail_thumb1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='fullname',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
