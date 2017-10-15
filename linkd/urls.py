# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from . import views
app_name = 'linkd'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    #url(r'^(?P<string>[\w\-]+)$',views.index,name='indexsearch'),
    url(r'^search$',views.search,name='search'),
    url(r'^form$',views.form,name='form'),
    url(r'^readform$',views.readform,name='readform'),
    url(r'^getmentor/(?P<mentor_id>[0-9]+)$',views.getmentor,name='getmentor')

]
