from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(about)
class about_admin(admin.ModelAdmin):
    fields = ('description', 'img')
    def __str__(self):
        return f"{self.description}"

@admin.register(event)
class events_admin(admin.ModelAdmin):
    fields = ('title', 'text', 'location', 'date_time', 'urls', 'img')
    def __str__(self):
        return f"{self.title, self.text}"
    
@admin.register(contact)
class contact_admin(admin.ModelAdmin):
    fields = ('text', 'email', 'phone')
    def __str__(self):
        return f"{self.text, self.email}"
    
@admin.register(member)
class member_admin(admin.ModelAdmin):
    fields = ('name', 'description', 'year', 'linkedin', 'img')
    def __str__(self):
        return f"{self.name, self.description, self.year}"
    
@admin.register(faq)
class faq_admin(admin.ModelAdmin):
    fields = ('question', 'answer', 'img')
    def __str__(self):
        return f"{self.question, self.answer}"
    
@admin.register(user)
class user_admin(admin.ModelAdmin):
    fields = ('posts', 'comments', 'liked_posts', 'liked_comments')
    def __str__(self):
        return f"{self.username}"
    
@admin.register(post)
class post_admin(admin.ModelAdmin):
    fields = ('title', 'text', 'img', 'date_time', 'comments', 'likes', 'user', 'links')
    def __str__(self):
        return f"{self.title, self.text}"
    
@admin.register(comment)
class comment_admin(admin.ModelAdmin):
    fields = ('text', 'user', 'date_time', 'likes')
    def __str__(self):
        return f"{self.text}"