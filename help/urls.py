from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'help'

urlpatterns = [
    path('', views.helps, name='helps'),
    path('<int:help_id>/', views.help, name='help'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)