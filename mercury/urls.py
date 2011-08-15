from django.conf.urls.defaults import *

from views import upload_image, save_content

urlpatterns = patterns('',
    url(r'^image$', upload_image, name='mercury-upload-image'),
    url(r'^save_content$', save_content, name='mercury-save-content'),
)
