# from bleach_whitelist import markdown_tags, markdown_attrs
from bleach import clean
from django import template
from django.utils.text import slugify
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import mistune
import re

register = template.Library()


class SPSRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return f'\n<pre><code>{mistune.escape(code)}</code></pre>\n'
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)
    
    def header(self, text, level, raw=None):
        # remove html tags and slugify title
        HTML_TAG_RE = re.compile(r'<[^>]+>')
        id_tag = slugify(HTML_TAG_RE.sub('', text))
        # return header html with id
        return f'\n<h{level} id="{id_tag}">{text}</h{level}>\n'

    def image(self, src, title, alt_text):
        if title is not None:
            title = f'title="{mistune.escape(title)}"'
        if alt_text is not None:
            alt_text = f'alt="{mistune.escape(alt_text)}"'
        # lazyload version
        lazyload = f'<img class="lazy" {alt_text} {title} data-src="{mistune.escape(src)}"' + \
                   'src="/static/images/1x1.png" >'
        # noscript fallback
        noscript = f'<noscript><img {alt_text} {title} src="{mistune.escape(src)}"></noscript>'
        return noscript + lazyload


def clean_html(html):
    # define allowed html tags and attributes
    markdown_tags = [
        "h1", "h2", "h3", "h4", "h5", "h6",
        "b", "i", "strong", "em", "tt",
        "p", "br",
        "span", "div", "blockquote", "code", "hr", "pre",
        "ul", "ol", "li", "dd", "dt",
        "img",
        "a",
        "sub", "sup",
        "noscript"
    ]
    markdown_attrs = {
        "*": ["id", "class"],
        "img": ["src", "data-src", "alt", "title"],
        "a": ["href", "alt", "title"],
    }
    # clean html
    cleaned = clean(html, markdown_tags, markdown_attrs)
    return cleaned


@register.filter
def markdown(value):
    # parse markdown
    renderer = SPSRenderer()
    md = mistune.Markdown(renderer=renderer)
    raw_html = md(value)
    # clean html
    cleaned_html = clean_html(raw_html)
    return cleaned_html
