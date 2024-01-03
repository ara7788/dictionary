from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import TermDetailView

app_name = 'term'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:term_id>/', views.term, name='term'),
    path('<char_name>/', views.terms, name='terms'),
    path('allterms/', views.allterms, name='allterms'),
    path("<slug:slug>", views.TermDetailView.as_view(), name="term_detail"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)