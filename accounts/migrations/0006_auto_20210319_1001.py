# Generated by Django 3.1.7 on 2021-03-19 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20210319_0009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='thumb1',
            new_name='displayphoto',
        ),
    ]