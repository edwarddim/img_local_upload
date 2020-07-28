from django.db import models

# Create your models here.
class Post(models.Model):
    subject = models.CharField(max_length=255, default=None, blank=True, null=True)
    file_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    image = models.ImageField(upload_to="profile", default=None, blank=True, null=True)