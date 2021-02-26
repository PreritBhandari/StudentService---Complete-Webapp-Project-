# Generated by Django 2.1 on 2021-02-26 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('faculty', models.CharField(choices=[('BCT', 'Computer'), ('BEL', 'Electrical'), ('BEX', 'Electronics'), ('BCE', 'Civil')], default='BCT', max_length=10)),
                ('year', models.CharField(choices=[('1st', 'First'), ('2nd', 'Second'), ('3rd', 'Third'), ('4th', 'Fourth')], default='1st', max_length=10)),
                ('roll_no', models.CharField(default='BCT074047', max_length=9)),
                ('fees_type', models.CharField(choices=[('monthly', 'monthly'), ('annual', 'annual')], max_length=10)),
                ('fee_month', models.CharField(blank=True, choices=[('jan', 'January'), ('feb', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('sept', 'Sept'), ('oct', 'October'), ('nov', 'November'), ('dec', 'December')], max_length=1000)),
                ('fee_paid_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.IntegerField(default=5000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=30)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.FileField(upload_to='media/files/')),
                ('details', models.CharField(default='No Details', max_length=30)),
                ('faculty', models.CharField(choices=[('BCT', 'Computer'), ('BCE', 'Electrical'), ('BEX', 'Electronics')], default='BCT', max_length=10)),
                ('year', models.CharField(choices=[('1st', 'First'), ('2nd', 'Second'), ('3rd', 'Third'), ('4th', 'Fourth')], default='3rd', max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(default='Prerit Bhandari', max_length=100)),
                ('faculty', models.CharField(choices=[('BCT', 'Computer'), ('BCE', 'Electrical'), ('BEX', 'Electronics')], max_length=10)),
                ('roll_no', models.CharField(default='074047', max_length=6)),
                ('total_annual_fee', models.IntegerField(default=1000000)),
                ('paid_annual_fee', models.IntegerField()),
                ('remaining_annual_fee', models.IntegerField()),
                ('last_annual_date_modified', models.DateTimeField(default=django.utils.timezone.now)),
                ('total_monthly_fee', models.IntegerField(default=5000)),
                ('paid_monthly_fee', models.IntegerField()),
                ('remaining_monthly_fee', models.IntegerField()),
                ('last_monthly_date_modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Fullfee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fees_type', models.CharField(choices=[('monthly', 'monthly'), ('annual', 'annual')], max_length=10)),
                ('fee_paid_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('fee_month', models.CharField(blank=True, choices=[('jan', 'January'), ('feb', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'), ('june', 'June'), ('july', 'July'), ('august', 'August'), ('sept', 'Sept'), ('oct', 'October'), ('nov', 'November'), ('dec', 'December')], max_length=1000)),
                ('amount_fee', models.CharField(max_length=10)),
                ('details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Fee')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
