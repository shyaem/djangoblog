# Generated by Django 3.1.7 on 2021-03-19 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20210305_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumb',
        ),
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(blank=True, default='default1.png', upload_to=''),
        ),
    ]