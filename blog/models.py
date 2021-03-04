from django.db import models
from django.db.models import IntegerField
from django.utils import timezone
# from django.contrib.auth.models import User
from django.urls import reverse

from users.models import CustomUser


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
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-post')


class Fullfee(models.Model):
    faculties = [

        ('BCT', 'Computer'),
        ('BCE', 'Electrical'),
        ('BEX', 'Electronics')

    ]
    type = [

        ('monthly', 'monthly'),
        ('annual', 'annual')

    ]

    month = [

        ('jan', 'January'),
        ('feb', 'February'),

        ('march', 'March'),
        ('april', 'April'),

        ('may', 'May'),
        ('june', 'June'),

        ('july', 'July'),
        ('august', 'August'),

        ('sept', 'Sept'),
        ('oct', 'October'),

        ('nov', 'November'),
        ('dec', 'December')

    ]

    details = models.ForeignKey(Fee, on_delete=models.CASCADE)
    fees_type = models.CharField(max_length=10, choices=type)
    fee_paid_date = models.DateTimeField(default=timezone.now)
    fee_month = models.CharField(max_length=1000, choices=month, blank=True)
    amount_fee = models.CharField(max_length=10)

    def __str__(self):
        return self.fee_month

    def get_absolute_url(self):
        return reverse('add-fee')


class Book(models.Model):
    faculties = [

        ('BCT', 'Computer'),
        ('BCE', 'Electrical'),
        ('BEX', 'Electronics')

    ]

    years = [

        ('1st', 'First'),
        ('2nd', 'Second'),
        ('3rd', 'Third'),
        ('4th', 'Fourth')

    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    thumbnail = models.ImageField(default='media/thumbnails/bookdefault.jpg', upload_to='media/thumbnails/', blank=True)
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    date = models.DateTimeField(default=timezone.now)
    file = models.FileField(upload_to='media/files/')
    details = models.CharField(max_length=30, default='No Details')
    faculty = models.CharField(max_length=10, choices=faculties, default='BCT')
    year = models.CharField(max_length=3, choices=years, default='3rd')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_list')


class AddFee(models.Model):
    faculties = [

        ('BCT', 'Computer'),
        ('BEL', 'Electrical'),
        ('BEX', 'Electronics'),
        ('BCE', 'Civil')

    ]

    years = [

        ('1st', 'First'),
        ('2nd', 'Second'),
        ('3rd', 'Third'),
        ('4th', 'Fourth')

    ]

    month = [

        ('jan', 'January'),
        ('feb', 'February'),

        ('march', 'March'),
        ('april', 'April'),

        ('may', 'May'),
        ('june', 'June'),

        ('july', 'July'),
        ('august', 'August'),

        ('sept', 'Sept'),
        ('oct', 'October'),

        ('nov', 'November'),
        ('dec', 'December')

    ]

    type = [

        ('monthly', 'monthly'),
        ('annual', 'annual')

    ]

    month = [

        ('jan', 'January'),
        ('feb', 'February'),

        ('march', 'March'),
        ('april', 'April'),

        ('may', 'May'),
        ('june', 'June'),

        ('july', 'July'),
        ('august', 'August'),

        ('sept', 'Sept'),
        ('oct', 'October'),

        ('nov', 'November'),
        ('dec', 'December')

    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    faculty = models.CharField(max_length=10, choices=faculties, default='BCT')
    year = models.CharField(max_length=10, choices=years
                            , default='1st')
    roll_no = models.CharField(max_length=9, default='BCT074000')
    is_hostel = models.BooleanField()
    fees_type = models.CharField(max_length=10, choices=type)
    fee_month = models.CharField(max_length=1000, choices=month, blank=True)
    fee_paid_date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField(default=5000)

    def __str__(self):
        return f' {self.name} {self.fees_type} fees'

    def get_absolute_url(self):
        return reverse('account-list')
