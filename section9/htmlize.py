from functools import singledispatch
from collections import abc
import fractions
import html
import decimal
import numbers

@singledispatch
def htmlize(obj:object) -> str:
    content = html.escape(repr(obj))
    return f'<pre>{content}</pre>'

@htmlize.register
def _(text:str) -> str:
    content = html.escape(text).replace('\n', '<br/>\n')
    return f'<p>{content}</p>'

@htmlize.register
def _(seq:abc.Sequence) -> str:
    inner = '<\li>\n<li>'.join(htmlize(item) for item in seq)
    return f'<ul>\n<li>' + inner + '</li>\n</ul>'

@htmlize.register
def _(n:numbers.Integral) -> str:
    return f'<pre>{n} (0x{n:x})</pre>'