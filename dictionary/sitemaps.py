from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from article.models import Article
from onlinehelper.models import OnlineHelper
from framework.models import Framework
from lection.models import Lection
from term.models import Term

class ArticleSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Article.objects.all()

    def lastmod(self, obj):
        return obj.mdate

class OnlineHelperSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return OnlineHelper.objects.all()

    def lastmod(self, obj):
        return obj.mdate

class FrameworkSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Framework.objects.all()

    def lastmod(self, obj):
        return obj.mdate

class LectionSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Lection.objects.all()

    def lastmod(self, obj):
        return obj.mdate
    
class TermSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Term.objects.all()

    def lastmod(self, obj):
        return obj.mdate
    
class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return ['contacts','signupuser','loginuser','logoutuser']

    def location(self, item):
        return reverse(item)