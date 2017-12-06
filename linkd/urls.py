# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from LinkIdProject import settings

app_name = 'linkd'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    #url(r'^(?P<string>[\w\-]+)$',views.index,name='indexsearch'),
    url(r'^search$',views.search,name='search'),
    url(r'^form$',views.form,name='form'),
    url(r'^readform$',views.readform,name='readform'),
    url(r'^getmentor/(?P<mentor_id>[0-9]+)$',views.getmentor,name='getmentor')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
