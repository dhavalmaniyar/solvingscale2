
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

class Inquiry(models.Model):
    name=models.CharField(max_length=30)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=256)
    inquiry=models.CharField(max_length=50)
    # pay=models.CharField(max_length=100)
    need=models.TextField()
    date=models.DateField(default=timezone.now())

class User(models.Model):
    user=models.TextField(default=None)
    def __str__(self):
        return self.user

class UserCount(models.Model):
    ucount=models.IntegerField()
    def __str__(self):
        return str(self.ucount)

class Snippet(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(blank=True, null=True)
    body = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def get_absolute_url(self):
        return f'/{self.slug}'

