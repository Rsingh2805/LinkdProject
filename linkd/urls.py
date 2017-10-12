# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url
from . import views
app_name = 'linkd'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^form$',views.form,name='form'),
    url(r'^readform$',views.readform,name='readform'),

]
