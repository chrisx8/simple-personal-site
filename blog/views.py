from django.conf import settings
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from home.models import SiteInfo
from .models import Article, Tag



def blog(request):
    articles = Article.objects.order_by('-last_edited', 'title')
    paginator = Paginator(articles, settings.BLOG_ARTICLES_PER_PAGE)
    # get page numbers as url param. Default to page 1
    page = request.GET.get('page')
    if page is None:
        page = 1
    # go to page 1 if invalid
    try:
        page = int(page)
        assert(1 <= page <= paginator.num_pages)
    except (AssertionError, ValueError):
        return HttpResponseRedirect(reverse('blog'))
    articles_on_page = paginator.get_page(page)
    # one page number before/after current
    if int(page)-2 >= 0:
        display_page_range = paginator.page_range[int(page)-2:int(page)+1]
    else:
        display_page_range = paginator.page_range[:int(page)+1]
    context = {
        'articles': articles_on_page,
        'page_range': display_page_range,
    }
    return render(request, 'blog.html', context=context)


def filter_by_tag(request, tag):
    # query tag
    try:
        tag_obj = Tag.objects.get(tag=tag)
        articles = Article.objects.filter(tag=tag_obj).order_by('-last_edited', 'title')
        assert articles
    except (Tag.DoesNotExist, AssertionError):
        raise Http404
    # find by tag and exclude hidden articles
    paginator = Paginator(articles, settings.BLOG_ARTICLES_PER_PAGE)
    # get page numbers as url param. Default to page 1
    page = request.GET.get('page')
    if page is None:
        page = 1
    # go to page 1 if invalid
    try:
        page = int(page)
        assert(1 <= page <= paginator.num_pages)
    except (AssertionError, ValueError):
        return HttpResponseRedirect(reverse('blog'))
    articles_on_page = paginator.get_page(page)
    # one page number before/after current
    if int(page)-2 >= 0:
        display_page_range = paginator.page_range[int(page)-2:int(page)+1]
    else:
        display_page_range = paginator.page_range[:int(page)+1]
    context = {
        'articles': articles_on_page,
        'page_range': display_page_range,
        'tag': tag,
    }
    return render(request, 'filter_by_tag.html', context=context)


def view_article(request, article_id):
    try:
        article = Article.objects.get(article_id=article_id)
    except Article.DoesNotExist:
        raise Http404
    context = {
        'article': article,
        'SITE_DESCRIPTION': article.subtitle
    }
    return render(request, 'view_article.html', context=context)
