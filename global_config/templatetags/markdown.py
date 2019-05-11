# from bleach_whitelist import markdown_tags, markdown_attrs
from bleach import clean
from django import template
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import mistune

register = template.Library()


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)


@register.filter
def markdown(value):
    # parse markdown
    renderer = HighlightRenderer()
    md = mistune.Markdown(renderer=renderer)
    html = md(value)
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
    ]
    markdown_attrs = {
        "*": ["id", "class"],
        "img": ["src", "alt", "title"],
        "a": ["href", "alt", "title"],
    }
    # clean html
    html = clean(html, markdown_tags, markdown_attrs)
    return html
