"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Monday, January 4, 2016
"""

# Imports
from django.db import models
from django.contrib.auth.models import User

"""
Category
Model class
Model Reference : /Cronometraje/Sistema/UML.doc > Events
"""
class Category( models.Model ) :
    # See UML definition for fields
    user = models.ForeignKey( User, default = 1 )
    name = models.CharField( max_length = 200, default = '' )
    description = models.TextField( max_length = None, default = '' )
    age_1 = models.IntegerField( default = 0 )
    age_2 = models.IntegerField( default = 0 )
    color = models.CharField( max_length = 200, default = '', unique = False )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Return the stringable model value """
        return self.name
    # End of unicode function
    
# End of Category Model

"""
CompetitionType
Model class
Model Reference : /Cronometraje/Sistema/UML.doc > Events
"""
class CompetitionType( models.Model ) :
    # See UML definition for fields
    name = models.CharField( max_length = 200, default = '' )
    description = models.TextField( max_length = None, default = '' )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Return the stringable model value """
        return self.name
    # End of unicode function
    
# End of competition type model

"""
Event type
Model class
Moel Reference : This is not in the UML :(
"""
class EventType( models.Model ) :
    
    name = models.CharField( max_length = 200, default = '' )
    description = models.TextField( max_length = None, default = '' )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False ) # Date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True ) # Date updated
    
    def __unicode__(self) :
        """ Unicode function print the object and shit """
        return self.name
    # End of unicode function
    
# End of EventType class model

"""
Event
Model class
Model Reference : /Cronometraje/Sistema/UML.doc > Events
"""
class Event( models.Model ) :
    # See UML definition for fields
    user = models.ForeignKey( User, default = 1 )
    name = models.CharField( max_length = 200, default = '' )
    description = models.TextField( max_length = None, default = '' )
    date_start = models.DateTimeField( blank = True )
    date_finish = models.DateTimeField( blank = True )
    image_url = models.TextField( max_length = None, default = '', blank=True )
    date_limit = models.DateTimeField( blank = True )
    competitors_limit = models.IntegerField( default = 1 )
    event_type = models.ForeignKey( EventType, default = 1 )
    address = models.TextField( max_length = None, default = '', blank=True )
    
    ubication = models.CharField( max_length = 500, default = '' )
    orginizer = models.CharField( max_length = 500, default = '', blank=True )
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Return the stringable model value """
        return self.name
    # End of unicode function
    
# End of event model

"""
Competition
Model class
Model Reference : /Cronometraje/Sistema/UML.doc > Events
"""
class Competition( models.Model ) :
    # See UML definition for fields
    user = models.ForeignKey( User, default = 1 )
    name = models.CharField( max_length = 200, default = '' )
    description = models.TextField( max_length = None, default = '' )
    date_start = models.DateTimeField( blank = True )
    date_finish = models.DateTimeField( blank = True )
    image_url = models.TextField( max_length = None, default = '', blank = True )
    categories = models.ManyToManyField( 'events.Category', blank = True )
    competition_type = models.ForeignKey( CompetitionType, default = 1 )
    competitors_limit = models.IntegerField( default = 0 )
    competition_event = models.ForeignKey( 'events.Event', default = 1 )
    cost = models.IntegerField( default = 0 )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Return the stringable model value """
        return self.name
    # End of unicode function
    
# End of competition model 

"""
In this we will add all the images to 
the event as a url from imgur.com
"""
class Galery( models.Model ) :
    # The event we are going to add the gallery
    event = models.ForeignKey( 'events.Event', default=1 )
    # The image url srtring of the image duuuh
    image_url = models.TextField( max_length = None, default='', blank = True )
    # Unicode function, almost important
    def __unicode__(self):
        """ Return the stringable model value """
        return self.image_url
    # End of unicode function
# End of Galery Model class

"""
In this we will add all the images to 
the event as a url from imgur.com
"""
class Conv( models.Model ) :
    # The event we are going to add the gallery
    event = models.ForeignKey( 'events.Event', default=1 )
    # The image url srtring of the image duuuh
    image_url = models.TextField( max_length = None, default='', blank = True )
    # Unicode function, almost important
    def __unicode__(self):
        """ Return the stringable model value """
        return self.image_url
    # End of unicode function
# End of Galery Model class

"""
This is a premio, i don't know if I put it well
"""
class Price( models.Model ) :
    
    name = models.CharField( max_length = 200, default = '' )
    description = models.TextField( max_length = None, default = '' )
    image_url = models.TextField( max_length = None, default = '', blank = True )
    event = models.ForeignKey( 'events.Event', default = 1 )
    
    timestamp = models.DateTimeField( auto_now_add = True, auto_now = False )#date created
    updated = models.DateTimeField( auto_now_add = False, auto_now = True )#date updated
    
    def __unicode__( self ) :
        """ Return the stringable model value """
        return self.name
    # End of unicode function
    
# End of Price model class