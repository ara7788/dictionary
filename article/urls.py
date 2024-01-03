from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.articles, name='articles'),
    path('<int:article_id>/', views.article, name='article'),
    path("<slug:slug>", views.ArticleDetailView.as_view(), name="article_detail"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)