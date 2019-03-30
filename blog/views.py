from django.core.paginator import Paginator
from django.shortcuts import render, Http404, HttpResponseRedirect
from django.urls import reverse
from simple_personal_site.site_config import ARTICLES_PER_PAGE, BLOG_DESCRIPTION
from .models import Article


def blog(request):
    # exclude hidden articles
    articles = Article.objects.filter(show=True).order_by('-time_posted')
    paginator = Paginator(articles, ARTICLES_PER_PAGE)
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
        'SITE_DESCRIPTION': f'{BLOG_DESCRIPTION} Check out my latest article: "{articles.first().title}"'
    }
    return render(request, 'blog.html', context=context)


def view_article(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404
    if not article.show:
        raise Http404
    context = {'article': article, 'SITE_DESCRIPTION': article.subtitle}
    return render(request, 'view_article.html', context=context)
