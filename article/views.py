from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Article

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article/article.html"

def articles(request):
    articles = Article.objects.order_by('-cdate')
    # Only 5 posts on page
    # articles = Article.objects.order_by('-cdate')[:3]
    return render(request,'article/articles.html', {'articles':articles})

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request,'article/article.html',{'article':article})

