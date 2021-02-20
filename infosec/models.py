from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.


class Information(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='infosec')

    def __str__(self):
        return f'{self.user.username} Information '

    def save(self, *args, **kwargs):
        if self.pk:
            this_record = Information.objects.get(pk=self.pk)
            if this_record.resume != self.resume:
                this_record.resume.delete(save=False)
        super(Information, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('infosec')
