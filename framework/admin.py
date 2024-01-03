from django.contrib import admin
from .models import Framework

class FrameworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'frameworkgroup')
    prepopulated_fields = {'slug': ('title', )}
    
admin.site.register(Framework, FrameworkAdmin)