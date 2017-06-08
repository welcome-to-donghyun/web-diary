from django.conf import settings
from django.db import models

class Memo(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)

class Diary(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    date = models.CharField(max_length=50)
    img = models.ImageField(
        null=True,
        upload_to='diary/',
    )

    def __str__(self):
        return str(self.title)
