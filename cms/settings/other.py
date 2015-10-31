# coding=utf-8
import os
from .base import BASE_DIR

DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'enjoyafrru_sa',
         'USER': 'enjoyafrru_sa',
         'PASSWORD': 'alena2010',
         'HOST': 'localhost',
         'PORT': '',
     }
}

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '../templates'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../../static')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '../static'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../../media')

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'default': {
        # 'width': 700,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['FontSize', 'TextColor'],
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Image'],
            ['RemoveFormat', 'Source']
        ]
    },
}

WHY_ICON_SIZE = [100, 100]
DOC_IMAGE_SIZE = [274, 392]
PHOTO_IMAGE_SIZE = [347, 335]
REVIEW_PHOTO_SIZE = [200, 200]
EXCURSE_COVER_SIZE = [360, 199]
GROUP_COVER_SIZE = [271, 217]
TRAVEL_COVER_SIZE = [370, 200]

INPLACEEDIT_EDIT_EMPTY_VALUE = 'Double click to edit'
INPLACEEDIT_AUTO_SAVE = True
INPLACEEDIT_EVENT = "dblclick"
INPLACEEDIT_SUCCESS_TEXT = u'Изменения сохранены'
INPLACEEDIT_UNSAVED_TEXT = u'У вас есть несохранённые изменения'