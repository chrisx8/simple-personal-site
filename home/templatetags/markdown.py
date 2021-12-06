from bleach import clean
from django import template
from django.utils.text import slugify
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import mistune
import re

register = template.Library()


class SPSRenderer(mistune.HTMLRenderer):
    def block_code(self, code, lang=None):
        if not lang:
            return f'\n<pre><code>{mistune.escape(code)}</code></pre>\n'
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)
    
    def heading(self, text, level):
        # remove html tags and slugify title
        HTML_TAG_RE = re.compile(r'<[^>]+>')
        id_tag = slugify(HTML_TAG_RE.sub('', text))
        # return header html with id
        return f'\n<h{level} id="{id_tag}">{text}</h{level}>\n'

    def image(self, src, alt="", title=None):
        if title:
            title = f'title="{mistune.escape(title)}"'
        if alt:
            alt = f'alt="{mistune.escape(alt)}"'
        return f'<img {alt} {title} src="{mistune.escape(src)}">'


def clean_html(html):
    # define allowed html tags and attributes
    markdown_tags = [
        "h1", "h2", "h3", "h4", "h5", "h6",
        "b", "i", "strong", "em", "tt",
        "p", "br",
        "span", "div", "blockquote", "code", "hr", "pre",
        "ul", "ol", "li", "dd", "dt",
        "table", "thead", "tbody", "tr", "th", "td",
        "img",
        "a",
        "sub", "sup"
    ]
    markdown_attrs = {
        "*": ["id", "class"],
        "img": ["src", "alt", "title"],
        "a": ["href", "alt", "title"],
    }
    # clean html
    cleaned = clean(html, markdown_tags, markdown_attrs)
    return cleaned


@register.filter
def markdown(value):
    # parse markdown
    renderer = SPSRenderer(escape=False)
    md = mistune.Markdown(renderer=renderer)
    raw_html = md(value)
    # clean html
    cleaned_html = clean_html(raw_html)
    return cleaned_html
