from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Information(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='infosec', default='infosec/Prerits_Resume.pdf', blank=True)
    website = models.CharField(max_length=200, default='www.studentservice.com', blank=True)
    github_link = models.CharField(max_length=200, default='github.com', blank=True)
    facebook_link = models.CharField(max_length=200, default='facebook.com', blank=True)
    linkedin_link = models.CharField(max_length=200, default='linkedin.com', blank=True)

    def __str__(self):
        return f'{self.user.username} Information'

    def save(self, *args, **kwargs):
        if self.pk:
            this_record = Information.objects.get(pk=self.pk)
            if this_record.resume != self.resume:
                this_record.resume.delete(save=False)
        super(Information, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('infosec')
