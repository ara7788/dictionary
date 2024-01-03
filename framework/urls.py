from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'framework'

urlpatterns = [
    path('', views.frameworks, name='frameworks'),
    path('<int:framework_id>/', views.framework, name='framework'),
    path("<slug:slug>", views.FrameworkDetailView.as_view(), name="framework_detail"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)