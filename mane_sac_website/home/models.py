from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
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

class email_list(models.Model):
    email = models.EmailField(blank=False)

    class Meta:
        verbose_name_plural = "Email List"

from django.contrib.auth.models import AbstractUser
from django.db import models

class user(AbstractUser):
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    posts = models.ManyToManyField('post', blank=True, related_name='user_posts')
    comments = models.ManyToManyField('comment', blank=True, related_name='user_comments')
    liked_posts = models.ManyToManyField('post', blank=True, related_name='liked_by_users')
    liked_comments = models.ManyToManyField('comment', blank=True, related_name='liked_by_users')
    
    groups = models.ManyToManyField(
        'auth.Group', blank=True, related_name="custom_user_groups"
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', blank=True, related_name="custom_user_permissions"
    )

class post(models.Model):
    title = models.TextField(blank=False)
    text = models.TextField(blank=False)
    img = models.ImageField(upload_to='posts/', null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField('comment', blank=True, related_name='post_comments')
    likes = models.IntegerField(default=0)
    user = models.ForeignKey('user', null=True, blank=True, on_delete=models.SET_NULL, related_name='user_posts')
    links = models.URLField(null=True, blank=True)

class comment(models.Model):
    text = models.TextField(blank=False)
    user = models.ForeignKey('user', null=True, blank=True, on_delete=models.SET_NULL, related_name='user_comments')
    date_time = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey('post', null=True, blank=True, on_delete=models.SET_NULL, related_name='comment_posts')
