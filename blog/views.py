from django.core.paginator import Paginator
from django.shortcuts import render, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Article, BlogConfig, Tag


def blog(request):
    try:
        # get blog config
        blog_config = BlogConfig.objects.get()
    except BlogConfig.DoesNotExist:
        # create blog config with defaults
        blog_config = BlogConfig()
        blog_config.save()
    # exclude hidden articles
    articles = Article.objects.order_by('-last_edited', 'title')
    paginator = Paginator(articles, blog_config.articles_per_page)
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
    try:
        latest_article = f'Check out my latest article: "{articles.first().title}"'
    except AttributeError:
        latest_article = ''
    context = {
        'articles': articles_on_page,
        'page_range': display_page_range,
        'SITE_DESCRIPTION': f'{blog_config.description} {latest_article}'
    }
    return render(request, 'blog.html', context=context)


def filter_by_tag(request, tag):
    try:
        # get blog config
        blog_config = BlogConfig.objects.get()
    except BlogConfig.DoesNotExist:
        # create blog config with defaults
        blog_config = BlogConfig()
        blog_config.save()
    # query tag
    try:
        tag_obj = Tag.objects.get(tag=tag)
        articles = Article.objects.filter(tag=tag_obj).order_by('-last_edited', 'title')
        assert len(articles)
    except (Tag.DoesNotExist, AssertionError):
        raise Http404
    # find by tag and exclude hidden articles
    paginator = Paginator(articles, blog_config.articles_per_page)
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
    try:
        latest_article = f'Check out my latest article: "{articles.first().title}"'
    except AttributeError:
        latest_article = ''
    context = {
        'articles': articles_on_page,
        'page_range': display_page_range,
        'tag': tag,
        'SITE_DESCRIPTION': f'{blog_config.description} {latest_article}'
    }
    return render(request, 'filter_by_tag.html', context=context)


def view_article(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    context = {'article': article, 'SITE_DESCRIPTION': article.subtitle}
    return render(request, 'view_article.html', context=context)
