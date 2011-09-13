from django.db import models
from django.contrib.admin import widgets as admin_widgets
from mercury import widgets as mercury_widgets
from tinymce import widgets as tinymce_widgets
from feincms.utils import get_object

from django.conf import settings

class HTMLField(models.TextField):
    """
    A large string field for HTML content. It uses the mercury widget in
    forms.
    """
    def formfield(self, **kwargs):
#        defaults = {'widget': mercury_widgets.TextareaMercury}
#        defaults.update(kwargs)
#
#        # As an ugly hack, we override the admin widget
#        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
#            defaults['widget'] = mercury_widgets.AdminTextareaMercury

        defaults = {'widget': tinymce_widgets.TinyMCE}
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = tinymce_widgets.AdminTinyMCE

        return super(HTMLField, self).formfield(**defaults) 

    def clean(self, value, model_instance):
        value = super(HTMLField, self).clean(value, model_instance)

        if settings.FEINCMS_TIDY_HTML:
            value, errors, warnings = get_object(settings.FEINCMS_TIDY_FUNCTION)(value )

        return value