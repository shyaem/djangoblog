# Generated by Django 3.1.7 on 2021-03-05 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210305_1109'),
    ]

    operations = [
        migrations.AddField(
            model_name='detail',
            name='thumb1',
            field=models.ImageField(blank=True, default='download.png', upload_to=''),
        ),
    ]
