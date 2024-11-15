from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class event(models.Model):
    title = models.TextField(blank=False)
    text = models.TextField(blank=False)
    location = models.TextField(null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    urls = models.URLField(null=True, blank=True)
    img = models.ImageField(upload_to='events/', null=True, blank=True)

class about(models.Model):
    description = models.TextField(blank=False)
    img = models.ImageField(upload_to='about/', null=True, blank=True)

    class Meta:
        verbose_name_plural = "About"

class contact(models.Model):
    text = models.TextField(blank=False, default = "For more information, please contact us at:")
    email = models.EmailField(blank=False)
    phone = models.CharField(max_length=10, blank=False)

class member(models.Model):
    name = models.TextField(blank=False)
    description = models.TextField(blank=False)
    year = models.TextField(blank=False)
    linkedin = models.URLField(null=True, blank=True)
    img = models.ImageField(upload_to='members/', null = True, blank = True)
    major = models.TextField(blank=False)

class faq(models.Model):
    question = models.TextField(blank=False)
    answer = models.TextField(blank=False)
    img = models.ImageField(upload_to='faq/', null = True, blank = True)

class email_list(models.Model):
    email = models.EmailField(blank=False)

    class Meta:
        verbose_name_plural = "Email List"

class post(models.Model):
    text = models.TextField(blank=False, null=False)
    img = models.ImageField(upload_to='posts/', null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    major = models.TextField(blank=True)
    year = models.TextField(blank=True)
    email = models.EmailField(blank=True)

