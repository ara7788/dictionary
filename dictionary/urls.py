"""
URL configuration for dictionary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from term import views
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ArticleSitemap, StaticSitemap, LectionSitemap, OnlineHelperSitemap, FrameworkSitemap, TermSitemap
from django.conf.urls import handler404, handler500

sitemaps = {
    'articles': ArticleSitemap,
    'lection': LectionSitemap,    
    'onlinehelper': OnlineHelperSitemap,
    'framework': FrameworkSitemap,
    'term': TermSitemap,
    'static': StaticSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signupuser,name='signupuser'),
    path('login/',views.loginuser,name='loginuser'),
    path('logout/',views.logoutuser,name='logoutuser'),

    path('',views.main, name='main'),
    path('home/', include('home.urls')),
    path('homecarusel',views.homecarusel, name='homecarusel'),
    path('term/', include('term.urls')),
    path('termsearch/', views.termsearch, name='termsearch'),
    path('allterms', views.allterms, name='allterms'),
    path('help/', include('help.urls')),
    path('contacts/', views.contacts, name='contacts'),
    path('article/', include('article.urls')),
    path('onlinehelper/', include('onlinehelper.urls')),
    path('framework/', include('framework.urls')),
    path('lection/', include('lection.urls')),
    path('rest/', include('api.urls')),
    path("react/", TemplateView.as_view(template_name="index.html")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('django-check-seo/', include('django_check_seo.urls')),
    # re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include('cms.urls')),
    re_path(r'^robots\.txt$',TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'term.views.view_404'
handler500 = 'term.views.view_500'