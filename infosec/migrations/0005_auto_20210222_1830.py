# Generated by Django 2.1 on 2021-02-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infosec', '0004_auto_20210220_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='resume',
            field=models.FileField(default='media/default.jpg', upload_to='infosec'),
        ),
    ]