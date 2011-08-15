from django.utils.simplejson import dumps, loads
from django.http import HttpResponse
from django.template import RequestContext, loader

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from django.core.files.base import ContentFile
from feincms.module.medialibrary.models import MediaFile
from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.utils import get_object

import re

from django.conf import settings

@csrf_protect
@login_required
def save_content(request):
    """
    content save handler
    Returns a HttpResponse whose content is JSON to tell if the operation succeeded.
    """
    result = {'result': False}

    if request.method == 'POST':
        if request.POST['content']:
            page_items = loads(request.POST['content'])

            for content_key, item in page_items.iteritems():
                # TODO: move to model/form cleaning

                content = item['value']
                if settings.FEINCMS_TIDY_HTML:
                    content , errors, warnings = get_object(settings.FEINCMS_TIDY_FUNCTION)(content)

                matches = re.search('^page-page-richtextcontent-(\d+)-(\d+)$', content_key)
                if matches:
                    page_id, content_id = matches.group(1), matches.group(2)

                    # TODO: replace with more flexible solution (not tied to the RichTextContent model), as done in _frontend_editing_view
                    RTC = Page.content_type_for(RichTextContent)
                    rtc = RTC.objects.get(id=content_id, parent__id=page_id)
                    rtc.text = content

                    rtc.save()
                    # TODO: this should be done differently; being able to handle every page-item separartly (see formsets)
                    result = {'result': True}

    return HttpResponse(dumps(result),
            content_type="application/json")

@csrf_protect
@login_required
def upload_image(request):
    """
    image upload handler
    Returns a HttpResponse whose content is JSON.
    """
    result = {'result': False}

    if request.method == 'POST' and request.FILES:
        if request.FILES['file']:
            # TODO: use form (validation)
            file = request.FILES['file']
            mf = MediaFile()
            mf.file.save(file.name, ContentFile(file.file.read()))
            mf.save()

            result = {'result': True}
            result['location'] = mf.get_absolute_url()

    return HttpResponse(dumps(result),
            content_type="application/json")