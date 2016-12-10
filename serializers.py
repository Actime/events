# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Tuesday, January 5, 2016
"""

# Imports
from rest_framework import serializers
from .models import Category, CompetitionType, Event, EventType, Competition, Galery, Price, Conv

"""
Category Serializer
Serializer Class
Model Reference : /Cronometraje/Sistema/UML.doc > Events
"""
class CategorySerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for serializer information
    """
    class Meta :
        model = Category
        fields = (
            'id',
            'user',
            'name',
            'description',
            'age_1',
            'age_2',
            'color',
        )
    # End of Meta class
    
# End of Category Serializer class

"""
CompetitionType Serializer
Serializer Class
Model Reference : /Cronometraje/Sistema/UML.doc > Events
"""
class CompetitionTypeSerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for serializer information
    """
    class Meta :
        model = CompetitionType
        fields = (
            'id',
            'name',
            'description',    
        )
    # End of Meta class
    
# End of CompetitionType Serializer class

"""
Event type serializer
serializer class
"""
class EventTypeSerializer( serializers.ModelSerializer ) :

    """
    Meta class for serializer information
    """
    class Meta :
        model = EventType
        fields = (
            'id',
            'name',
            'description',
        )
    # End of Meta class
    
# End of EventTypeSerializer class

"""
Event Serializer
Serializer Class
Model Reference : /Cronometraje/Sistema/UML.doc > Events
"""
class EventSerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for serializer information
    """
    class Meta :
        model = Event
        fields = (
            'id',
            'user',
            'name',
            'description',
            'date_start',
            'date_finish',
            'image_url',
            'date_limit',
            'competitors_limit',
            'event_type',
            'ubication',
            'orginizer',
            'address',
        )
    # End of Meta class
    
# End of Event Serializer class

"""
Competition Serializer
Serializer Class
Model Reference : /Cronometraje/Sistema/UML.doc > Events
"""
class CompetitionSerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for serializer information
    """
    class Meta :
        model = Competition
        fields = (
            'id',
            'user',
            'name',
            'description',
            'date_start',
            'date_finish',
            'image_url',
            'categories',
            'competition_type',
            'competitors_limit',
            'competition_event',
            'cost',
        )
    # End of Meta class
    
# End of Competition Serializer class

"""
Galery serializer class
"""
class GalerySerializer( serializers.ModelSerializer ) :
    
    """
    Meta class for serializer information
    """
    class Meta : 
        model = Galery
        fields = ( 
            'id', 
            'event',
            'image_url',
        )
    # End of meta class
# End of GalerySerializer class

class PriceSerializer( serializers.ModelSerializer ) :
    
    """
    Metca class for serializer information
    """
    class Meta :
        model = Price
        fields = (
            'id',
            'name',
            'description',
            'image_url',
            'event'
        )
    # End of meta class
# End of PriceSerializer class

class ConvSerializer( serializers.ModelSerializer ) : 
    
    """
    Meta class for serializer information
    """
    class Meta :
        model = Conv
        fields = (
            'id',
            'event',
            'image_url'
        )
    # End of meta class
# Edn fo conv serializer class 