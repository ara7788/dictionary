from django.contrib import admin
from .models import Term
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class TermAdmin(admin.ModelAdmin):
    list_display = ('title', 'cdate')
    prepopulated_fields = {'slug': ('title', )}

# Register your models here.
admin.site.register(Term, TermAdmin)


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())  # Поле моделей у нас назвается 'content', поэтому оставляем переменную без именений
    
    class Meta:
        model = Term  # Тут нужно указать название можеди в которой мы будем использовать CKEditor
        fields = '__all__'

form = NewsAdminForm