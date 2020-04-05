from django.db import models
from django.db.models import IntegerField
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Fee(models.Model):
    all_faculty = [

        ('BCT', 'Computer'),
        ('BCE', 'Electrical'),
        ('BEX', 'Electronics')

    ]

    fullname = models.CharField(max_length=100, default='Prerit Bhandari')
    faculty = models.CharField(max_length=10, choices=all_faculty)
    roll_no = models.CharField(max_length=6, default='074047')
    total_annual_fee = models.IntegerField(default=1000000)
    paid_annual_fee = models.IntegerField()
    remaining_annual_fee = models.IntegerField()
    last_annual_date_modified = models.DateTimeField(default=timezone.now)
    total_monthly_fee = models.IntegerField(default=5000)
    paid_monthly_fee = models.IntegerField()
    remaining_monthly_fee = models.IntegerField()
    last_monthly_date_modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.fullname


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-rate')
