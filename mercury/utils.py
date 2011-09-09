import bleach

ALLOWED_TAGS = [
    'div',
    'p', 'span',
    'a',
    'h2', 'h3', 'h4', 'h5', 'h6',
    'b', 'strong',
    'i', 'em',
    'ol', 'ul', 'li',
    'dl', 'dt', 'dd',
    'code', 'pre',
    'abbr', 'acronym', 'blockquote',
    'br',
    'img',
]

ALLOWED_ATTRIBUTES = {
    'h2':   ['class'],
    'h3':   ['class'],
    'h4':   ['class'],
    'h5':   ['class'],
    'h6':   ['class'],


    'div':  ['class'],
    'p':    ['class'],
    'span': ['class'],
    'a':    ['href', 'title', 'class', 'target'],

    'ol':   ['class'],
    'ul':   ['class'],
    'li':   ['class'],

    'dl':   ['class'],
    'dt':   ['class'],
    'dd':   ['class'],

    'abbr': ['title'],
    'acronym': ['title'],

    'img': ['class', 'src', 'alt', 'title', 'width', 'height'],
}

def sanitize(text, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES):
    "sanitize html"
    html = bleach.clean(text, strip=True, tags=tags, attributes=attributes, strip_comments=False)

    # strip empty tags
    return html.replace('<div></div>','').replace('<p></p>','')

def tidy(text):
    "sanitize wrapper in tidy interface"
    return (sanitize(text), None, None) # TODO: return errors and warnings