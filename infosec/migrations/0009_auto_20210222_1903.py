# Generated by Django 2.1 on 2021-02-22 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infosec', '0008_auto_20210222_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='facebook_link',
            field=models.CharField(blank=True, default='facebook.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='information',
            name='github_link',
            field=models.CharField(blank=True, default='github.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='information',
            name='linkedin_link',
            field=models.CharField(blank=True, default='linkedin.com', max_length=200),
        ),
        migrations.AlterField(
            model_name='information',
            name='resume',
            field=models.FileField(blank=True, default='infosec/Prerits_Resume.pdf', upload_to='infosec'),
        ),
        migrations.AlterField(
            model_name='information',
            name='website',
            field=models.CharField(blank=True, default='www.studentservice.com', max_length=200),
        ),
    ]
