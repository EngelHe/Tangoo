'''
Copyright (C) 2015 Netease All rights reserved
Author: hzhexin@corp.netease.com
Date: Tues Jul 7 2015
Description:
'''


from django.conf.urls import patterns, url
from rango import views


#empty string r'^$'

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^about/$', views.about, name='about'),
                       url(r'^register/$', views.register, name='register'),
                       url(r'^login/$', views.login, name='login'),
                       url(r'^add_category/$', views.add_category, name='add_category'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$', views.add_page, name='add_page'),
                       )

