# Generated by Django 2.1 on 2021-02-27 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('infosec', '0005_auto_20210227_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
