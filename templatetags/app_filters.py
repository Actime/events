# -*- coding: utf-8 -*-
"""
App_tags file
Author : Ramiro de Jesus gutierrez alaniz
Date : Sunday, January 31, 2016
"""
# All the improts
from django import template
from django.conf import settings
from events.models import Competition, Galery, Price, Conv
from competitors.models import Competitor, Register, TimeReg 
import os, json

# register varialbe for register the filters on the template library
register = template.Library()

@register.filter(name='get_all_competitions')
def get_all_competitions( value ) :
    """
    Get all competitions from the sended event
    """
    # return the competitions fo the event
    return Competition.objects.filter(competition_event=value.id)
# End of get_all_competitions function

@register.filter( name='get_all_categories' )
def get_all_categories( value ) :
    """
    Get all categories form the sended competition
    """
    # return the categories of the competition
    return value.categories.all()
# End of get_all_categories function

@register.filter( name='get_month' )
def get_month( value ) :
    """
    Returns the month of a date as a string
    Example; instead of 1 returns january
    """
    months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre' ]
    # Return the month value in string
    return months[value.month]
# End of get_month function

@register.filter( name='get_galery' )
def get_galery( value ) :
    """
    Returns the galery list of the event
    """
    # Filter the galery
    galery = Galery.objects.filter( event = value.pk )
    # Return the galery
    return galery
# End of get_galery function

@register.filter( name='get_all_conv' )
def get_all_conv( value ) : 
    """
    Returns the convocatories of the event
    """
    # Filter the convs
    convs = Conv.objects.filter( event = value.pk )
    # Return the convs
    return convs
# End of get_all_conv function

@register.filter( name='get_prices' )
def get_prices( value ):
    """
    This function returns all the prices from the event
    """
    return Price.objects.filter( event = value.pk )
# End of get_prices function

@register.filter( name='get_latitude' )
def get_latitude( value ) :
    """
    This will return the latitude of the event 99.1333
    """
    if not value.ubication :
        return "19.0000"
    else :
        attrs = value.ubication.strip().split(",")
        return attrs[0]
# End of get_latitude function

@register.filter( name='get_longitude' )
def get_longitude( value ) :
    """
    This will return the longitude of the event 
    """
    if not value.ubication :
        return "99.1333"
    else :
        attrs = value.ubication.strip().split(",")
        return attrs[1]
# End of get_latitude function

@register.filter( name="get_time_registers" )
def get_time_registers( value ) :
    """
    This will return the time registers from a competitor
    """
    time_regs = TimeReg.objects.filter( register = value.pk )
    # return the time registers
    return time_regs
# End of get_time_registers function

@register.filter(name="get_competitors_place_global")
def get_competitors_place_global( value, value2 ) :
    """
    this will return the competitor's time of an event
    value; this is the competitor
    value2¨; this is the competition
    """
    return "1st"
# End of get_competitors_time_ev function

@register.filter(name="get_competitors_place_cat")
def get_competitors_place_cat( value, value2 ) :
    """
    this will return the competitor's time of a categry
    value; this is the competitor
    value2¨; this is the competition
    """
    return "2nd"
# End of get_competitors_time_cat function

@register.filter(name="get_competitors_time")
def get_competitors_time( value, value2 ) :
    """
    This will return the competitor's time of the competence
    value; this is the competitor
    value2; this is the event
    """
    return "12hr:09m:34s"
# End of get_competitors_time function

@register.assignment_tag
def get_loads():# Get the contents
    """
    returns the contents of the headers and the footers
    """
    json_data = open( os.path.join( settings.BASE_DIR, 'static_pro', 'resources', 'general_resources.json') )
    #Context variable, is just fucking important, believe it
    return json.load(json_data)['content_es']
# End of get_loads function