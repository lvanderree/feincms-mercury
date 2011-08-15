from django import forms
from django.contrib.admin import widgets as admin_widgets

from django.forms.widgets import flatatt
from django.utils.safestring import mark_safe
from django.utils.html import escape
try:
    from django.utils.encoding import smart_unicode
except ImportError:
    from django.forms.util import smart_unicode

import mercury.settings

class TextareaMercury(forms.Textarea):
    def render(self, name, value, attrs=None):
        if value is None: value = ''
        value = smart_unicode(value)

        if not attrs.has_key('class'):
            attrs['class'] = 'mercury-region'
        else:
            attrs['class'] += ' mercury-region'
        attrs['data-type'] = 'editable'

        final_attrs = self.build_attrs(attrs)
        final_attrs['name'] = name

        html = [u'<textarea%s>%s</textarea>' % (flatatt(final_attrs), escape(value))]

        return mark_safe(u'\n'.join(html))

    def _media(self):
        js = [
            'mercury/javascripts/mercury_loader.js?pack=onsite',
        ]
        css = {
#            'screen': [] # done by loader
        }
        return forms.Media(js=js, css=css)
    media = property(_media)

class AdminTextareaMercury(admin_widgets.AdminTextareaWidget, TextareaMercury):
    def _media(self):
        js = [
            'mercury/javascripts/mercury_loader.js?pack=admin',
        ]
        css = {
#            'screen': [] # done by loader
        }
        return forms.Media(js=js, css=css)
    media = property(_media)

