from django.conf import settings
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from home.models import SiteInfo
from .models import Article, Tag


def blog(request, tag=None):
    articles = Article.objects.order_by('-last_edited', 'title')

    # validate tag: has to exist and have articles
    valid_tag = tag and Tag.objects.filter(tag=tag)
    has_articles_with_tag = valid_tag and articles.filter(tag=tag)
    # 404 if tag doesn't exist
    if tag and (not valid_tag or not has_articles_with_tag):
        raise Http404
    elif tag:
        # tag is valid. get articles with tag
        articles = articles.filter(tag=tag)

    paginator = Paginator(articles, settings.BLOG_ARTICLES_PER_PAGE)
    # get page numbers as url param. Default to page 1
    page = request.GET.get('page')
    if not page:
        page = 1
    # go to page 1 if invalid
    try:
        page = int(page)
        assert(1 <= page <= paginator.num_pages)
    except (AssertionError, ValueError):
        return HttpResponseRedirect(reverse('blog'))

    # one page number before/after current
    if int(page)-2 >= 0:
        display_page_range = paginator.page_range[int(page)-2:int(page)+1]
    else:
        display_page_range = paginator.page_range[:int(page)+1]
    # articles to show on page
    articles_on_page = paginator.get_page(page)

    context = {
        'articles': articles_on_page,
        'page_range': display_page_range,
    }

    # tag specified, show filter by tag page
    if tag:
        context['tag'] = tag
        return render(request, 'filter_by_tag.html', context=context)

    # no tag, show normal blog page
    return render(request, 'blog.html', context=context)


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
