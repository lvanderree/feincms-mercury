import bleach

ALLOWED_TAGS = [
    'div',
    'p', 'span',
    'a',
    'h2', 'h3', 'h4', 'h5', 'h6',
    'b', 'strong',
    'i', 'em',
    'ol', 'ul', 'li',
    'code', 'pre',
    'abbr', 'acronym', 'blockquote',
    'br', 'img',
]

ALLOWED_ATTRIBUTES = {
    'div':  ['class'],
    'p':    ['class'],
    'span': ['class'],
    'a':    ['href', 'title', 'class'],

    'ol':   ['class'],
    'ul':   ['class'],
    'li':   ['class'],

    'abbr': ['title'],
    'acronym': ['title'],

    'img': ['class', 'src', 'alt', 'title', 'width', 'height'],
}

def sanitize(text, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES):
    "sanitize html"
    return bleach.clean(text, strip=True, tags=tags, attributes=attributes, strip_comments=False)

def tidy(text):
    "sanitize wrapper in tidy interface"
    return (sanitize(text), None, None) # TODO: return errors and warnings