# Generated by Django 3.1.7 on 2021-03-05 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('displayname', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('dob', models.DateTimeField()),
                ('mobile', models.CharField(max_length=10, unique=True)),
                ('bio', models.TextField(max_length=130)),
            ],
        ),
    ]
