from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(about)
class about_admin(admin.ModelAdmin):
    fields = ('description', 'img')
    def __str__(self):
        return f"{self.description}"