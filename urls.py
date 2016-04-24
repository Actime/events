# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Sunday, January 31, 2016
"""
# Imports
from django.conf.urls import patterns, url
from .views import *

# General Url patterns result_detail
urlpatterns = patterns(
    
    'events.views',
    # Event index
    url( r'^$', event_index, name='views.event.index' ),
    # Events
    url( r'^(?P<pk>[0-9]+)$', event_detail, name='views.event.detail' ),
    # Competitions
    url( r'^competition/(?P<pk>[0-9]+)$', competiton_detail, name="views.competition.detail" ),
    # Results index
    url( r'^results/$', result_list, name="views.event.results" ),
    # Get search results
    url( r'^rd/search/(?P<pk>[0-9]+)$', search_results, name="views.event.results.search" ),
    # Result detail search_results
    url( r'^rd/(?P<pk>[0-9]+)$', result_detail, name="views.event.result.detail" ),
    
)# End of general sytem url patterns