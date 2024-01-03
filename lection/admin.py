from django.contrib import admin
from .models import Lection
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

class LectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_detail')
    prepopulated_fields = {'slug': ('title', )}

admin.site.register(Lection, LectionAdmin)

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())  # Поле моделей у нас назвается 'content', поэтому оставляем переменную без именений
    
    class Meta:
        model = Lection  # Тут нужно указать название можеди в которой мы будем использовать CKEditor
        fields = '__all__'

form = NewsAdminForm