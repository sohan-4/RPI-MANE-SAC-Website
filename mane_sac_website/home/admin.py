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