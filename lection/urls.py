from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'lection'

urlpatterns = [
    path('', views.lections, name='lections'),
    path('<int:lection_id>/', views.lection, name='lection'),
    path("<slug:slug>", views.LectionDetailView.as_view(), name="lection_detail"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)