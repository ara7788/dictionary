from django.contrib import admin
from .models import OnlineHelper

class OnlineHelperAdmin(admin.ModelAdmin):
    list_display = ('title', 'stream_framework_name')
    prepopulated_fields = {'slug': ('title', )}
    
admin.site.register(OnlineHelper, OnlineHelperAdmin)