from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.homes, name='homes'),
    path('<int:home_id>/', views.home, name='home'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)