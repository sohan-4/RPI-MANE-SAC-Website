from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class events(models.Model):
    title = models.TextField(blank=False)
    text = models.TextField(blank=False)
    location = models.TextField(null=True, blank=True)
    date_time = models.DateTimeField(null=True, blank=True)
    urls = models.URLField(null=True, blank=True)
    img = models.ImageField(upload_to='events/', null=True, blank=True)

class about(models.Model):
    description = models.TextField(blank=False)
    img = models.ImageField(upload_to='about/', null=True, blank=True)

class contact(models.Model):
    text = models.TextField(blank=False, default = "For more information, please contact us at:")
    email = models.EmailField(blank=False)
    phone = PhoneNumberField(blank=True)

class member(models.Model):
    name = models.TextField(blank=False)
    description = models.TextField(blank=False)
    year = models.TextField(blank=False)
    linkedin = models.URLField(null=True, blank=True)
    img = models.ImageField(upload_to='members/', null = False, blank = False)

class faq(models.Model):
    question = models.TextField(blank=False)
    answer = models.TextField(blank=False)
    img = models.ImageField(upload_to='faq/', null = True, blank = True)