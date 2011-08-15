from django.db import models
from django.contrib.admin import widgets as admin_widgets
from mercury import widgets as mercury_widgets

class HTMLField(models.TextField):
    """
    A large string field for HTML content. It uses the mercury widget in
    forms.
    """
    def formfield(self, **kwargs):
        defaults = {'widget': mercury_widgets.TextareaMercury}
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = mercury_widgets.AdminTextareaMercury

        return super(HTMLField, self).formfield(**defaults)
