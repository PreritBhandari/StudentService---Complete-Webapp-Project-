# Generated by Django 2.1 on 2021-02-20 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infosec', '0002_auto_20210220_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='resume',
            field=models.FileField(upload_to='infosec'),
        ),
    ]
