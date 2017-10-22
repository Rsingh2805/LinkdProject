from django.conf.global_settings import TEMPLATES

TEMPLATES[0]['OPTIONS']['context_processors']+='django.core.context_processors.request'