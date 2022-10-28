from django.db import models


# Create your models here.


class MyUser(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True),
    email = models.EmailField("email address", blank=True)
    phone = models.CharField("phone", blank=True, max_length=10)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=200, null=False, blank=True)

    class Meta:
        ordering = ['date_updated']

    def __str__(self):
        return self.username

    # objects = models.Manager()

