# -*- coding: utf-8 -*-
"""
Author - Ramiro Gutierrez Alaniz
Company - RestCont
Area - IT; B-E Develpment
Date - Wednesday, January 5, 2016
"""

# Imports
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.core import serializers
# Rest framework imports
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# Import classes 
from events.models import Event, Competition, CompetitionType, Category, EventType, Price, Galery
from competitors.models import Register, Competitor
from helpers.imgur import *
# Import Serializers
from events.serializers import EventSerializer, CompetitionSerializer, CompetitionTypeSerializer, CategorySerializer, EventTypeSerializer, PriceSerializer, GalerySerializer
# Image decode shit
from PIL import Image
from base64 import *
import datetime

"""
Price list api view
Lists all the awards and shit; I just messed up the name
"""
class PriceList( generics.ListCreateAPIView ) :
    # Authentication classes
    authentication_classes = ( BasicAuthentication, )
    # permission classes
    permission_classes = ( IsAuthenticated, )
    # query set definition
    queryset = Price.objects.all()
    # serializer class
    serializer_class = PriceSerializer
    # get queryset function
    def get_queryset(self) :
        """
        get_queryset
        function that returns the queryset of the api view class
        returns a queryset
        """
        # get the event id from the request
        event_id = self.request.GET['event_id']
        # get the object and then return it or return a 404 if it doesn't exist 
        event = get_object_or_404( Event, pk = event_id )
        # get the prices from the db
        prices = Price.objects.filter( event = event.id )
        # return the categories
        return prices
    # End of get_query
    
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of PriceSerializer class

class PriceDetail( generics.RetrieveUpdateDestroyAPIView ) :
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Price detail class

"""
EventList Api View
Object list and creation
"""
class EventList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Event.objects.all()
    # Serializer class
    serializer_class = EventSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Event List class

"""
Event Detail Api View
"""
class EventDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Event.objects.all()
    # Serializer class
    serializer_class = EventSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Event Detail class

class EventTypeList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = EventType.objects.all()
    # Serializer class
    serializer_class = EventTypeSerializer
    # list function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of EventTypeList class
    
"""
EventType Detail Api View
"""
class EventTypeDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = EventType.objects.all()
    # Serializer class
    serializer_class = EventTypeSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of EventType Detail class

"""
CompetitionList Api View
Object list and creation
"""
class CompetitionList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Competition.objects.all()
    # Serializer class
    serializer_class = CompetitionSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Competition List class

"""
Competition Detail Api View
"""
class CompetitionDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Competition.objects.all()
    # Serializer class
    serializer_class = CompetitionSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Competition Detail class

"""
CompetitionList Api View
Object list and creation
"""
class CompetitionListByEvent( generics.ListAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Competition.objects.all()
    # Serializer class
    serializer_class = CompetitionSerializer
    # Get query set definition
    def get_queryset(self) :
        """
        get_queryset
        function that returns the queryset of the api view class
        returns a queryset
        """
        # get the event id from the request
        event_id = self.request.GET['event_id']
        # filter the objects and then return them
        return Competition.objects.filter(competition_event=event_id)
    # End of get_query
    
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
    
# End of Competition List by Event class

"""
CompetitionTypeList Api View
Object list and creation
"""
class CompetitionTypeList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = CompetitionType.objects.all()
    # Serializer class
    serializer_class = CompetitionTypeSerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Competition Type List class

"""
Competition Type Detail Api View
"""
class CompetitionTypeDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = CompetitionType.objects.all()
    # Serializer class
    serializer_class = CompetitionTypeSerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Competition Type Detail class

"""
CategoryList Api View
Object list and creation
"""
class CategoryList( generics.ListCreateAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Category.objects.all()
    # Serializer class
    serializer_class = CategorySerializer
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of Category List class

"""
Category Detail Api View
"""
class CategoryDetail( generics.RetrieveUpdateDestroyAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Category.objects.all()
    # Serializer class
    serializer_class = CategorySerializer
    # Retrieve function definition
    def retrieve(self, request, *args, **kwargs):
        """ retrive the model with id """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = { 
            "data" : serializer.data
        }
        return Response(data)
    # End of retrieve function
# End of Category Detail class

"""
CategoryListByCompetition Api View
Object list and creation
"""
class CategoryListByCompetition( generics.ListAPIView ) :
    # Authentiction classes
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    # Query Set
    queryset = Category.objects.all()
    # Serializer class
    serializer_class = CategorySerializer
    # Get query set definition
    def get_queryset(self) :
        """
        get_queryset
        function that returns the queryset of the api view class
        returns a queryset
        """
        # get the event id from the request
        competition_id = self.request.GET['competition_id']
        # get the object and then return it or return a 404 if it doesn't exist 
        competition = get_object_or_404( Competition, pk = competition_id )
        # return the categories
        return competition.categories
    # End of get_query
    
    # List function definition
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
    
# End of Category List by Competition class

"""
Register competitor number
this will return the next competitor number of the event
"""
class RegisterCompetitorNumber( APIView ) :
    
    def get_object( self, pk ) :
        """
        Get object funciton
        This will return a competition
        """
        try :
            # Get the object by the primary key
            return Competition.objects.get( pk = pk )
        except Competition.DoesNotExist :
            # Return a 404 error if not found in the db
            raise Http404
    # End of get_object function
    
    def get( self, request, pk, format=None ) : 
        """
        Get function just for getting the fucking register number
        """
        # First get the competition by primary key
        competition = self.get_object( pk )
        # Get the event by competition 
        event = Event.objects.get( pk = competition.competition_event.pk )
        # Get all the competitions by event
        competitions = Competition.objects.filter( competition_event = event.pk )
        # Init an empty list of registers
        registers = list()
        # Get all registers by each competition
        for comp in competitions :
            temporal_registers = Register.objects.filter( competition = comp.pk )
            # Verify if the temporal registers are actually not null
            if temporal_registers is not None :
                # Merge the temporal registers to the registers list
                registers = registers + [entry for entry in temporal_registers]
        # End of for
        # validate if the registers list is empty
        if len(registers) :
            # Merge all by order of timestamp
            registers.sort(key=lambda x:x.timestamp, reverse=False)
            # Get the last competitors number
            last_competitor_num = registers[-1].competitor_num
            # data encaps, data bitch!!!!
            data = {
                'data' : (last_competitor_num + 1)   
            }
            # Return the last number plus one, the puls one is on the data encaps
            return Response( data )
        # If there is no register return 1
        else :
            data = {
                'data' : 1,    
            }
            return Response( data )
        # End of else
    # End of get function
# End of RegisterCompetitorNumber api view class

class GaleryList( generics.ListAPIView ) :
    # Authentication classes
    authentication_classes = ( BasicAuthentication, )
    # permission classes
    permission_classes = ( IsAuthenticated, )
    # query set definition
    queryset = Galery.objects.all()
    # serializer class
    serializer_class = GalerySerializer
    # get queryset function
    def get_queryset(self) :
        """
        get_queryset
        function that returns the queryset of the api view class
        returns a queryset
        """
        # get the event id from the request
        event_id = self.request.GET['event_id']
        # get the object and then return it or return a 404 if it doesn't exist 
        event = get_object_or_404( Event, pk = event_id )
        # get the prices from the db
        galeries = Galery.objects.filter( event = event.id )
        # return the categories
        return galeries
    # End of get_query
    
    def list( self, request, *args, **kwargs ):
        """ 
        list
        fuction that list all the objects of the model
        returns a serialized json response
        """
        instance = self.filter_queryset( self.get_queryset() )
        # Getp
        page = self.paginate_queryset( instance )
        # Verify pagination
        if page is not None :
            serializer = self.get_pagination_serializer( page )
        else:
            serializer = self.get_serializer( instance, many=True )
        # This format is for iOS to rec. the data in a better way
        data = {
            "data" : serializer.data
        }
        # Return response with json serialized data
        return Response( data )
    # End of list function 
# End of PriceSerializer class
# End of GaleryList view class

class GaleryDetail( generics.RetrieveUpdateDestroyAPIView ) :
    authentication_classes = ( BasicAuthentication, )
    permission_classes = ( IsAuthenticated, )
    queryset = Galery.objects.all()
    serializer_class = GalerySerializer
    def retrieve( self, request, *args, **kwargs ) :
        """ retrieve the model with id """
        instance = self.get_object()
        serializer = self.get_serializer( instance )
        data = { "data" : serializer.data }
        return Response( data )
    # End of retrieve function
# End of Galery Detail view class


class ImageToPrizeCreate( APIView ) :
    def get_object( self, pk ) :
        """
        Get object function
        """
        try :
            # Get the object by the primary key
            return Price.objects.get( pk=pk )
        except Price.DoesNotExist :
            # Return a 404 error if not found in the db
            raise Http404
    # End of get_object function
    def put( self, request, pk, format=None ) :
        """
        When postin the gallery image
        """
        # Get the object by primary key
        price = self.get_object( pk )
        # ^rize serializer
        price_serializer = PriceSerializer( price )
        # Get the images from the pettition
        fh = open( "imageToSave.png", "wb" )
        # Write the file
        fh.write( request.data.decode( "base64" ) )
        # Close the file
        fh.close()
        # Save the image on the price
        save_image_to_price( "imageToSave.png", price )
        # return the price serialized
        return Response( PriceSerializer( price ).data )
    # End of put function
# End of ImageTo Prize Create Class

"""
Add image to event
"""
class ImageToEventCreate( APIView ) : 
    
    def get_object( self, pk ) :
        """
        Get object function
        """
        try :
            # Get the object by the primary key
            return Event.objects.get( pk=pk )
        except Event.DoesNotExist :
            # Return a 404 error if not found in the db
            raise Http404
    # End of get_object function
    
    def put( self, request, pk, format=None ) :
        """
        when posting the event image
        """
        # Get the object by primary key
        event = self.get_object( pk )
        # Event serializer
        event_serializer = EventSerializer(event)
        # Get the images from the pettition
        fh = open("imageToSave.png", "wb")
        # Write on the file
        fh.write(request.data.decode('base64'))
        # Close the file
        fh.close()
        # Save the image on the event
        save_image_event( "imageToSave.png", event.id )
        # return the event serialized
        return Response(event_serializer.data)
    # End of post function
# End of Image To Event Create class

"""
Image to copmetition
this request is for saving the image on the imgur server app
all this of the competition model
"""
class ImageToCompetitionCreate( APIView ) :
    
    def get_object( self, pk ) :
        """
        Get object function
        """
        try :
            # Get the object by the primary key
            return Competition.objects.get( pk=pk )
        except Competition.DoesNotExist :
            # Return a 404 error if not found in the db
            raise Http404
    # End of get_object function
    
    def put( self, request, pk, format=None ) :
        """
        When postin the competition image
        """
        # Get the object by primary key
        competition = self.get_object( pk )
        print( competition )
        # Competition serializer
        copmetition_serializer = CompetitionSerializer( competition )
        # Get the images from the pettition
        fh = open( "imageToSave.png", "wb" )
        # Write the file
        fh.write( request.data.decode( "base64" ) )
        # Close the file
        fh.close()
        # Save the image on the competition
        save_image_competition( "imageToSave.png", competition.id )
        # return the competition serialized
        return Response( copmetition_serializer.data )
    # End of put function
# End of ImageToCompetitionCreate view class

"""
Image to galery
this request is for saving the image on the imgur server app
all this of the galery model
"""
class ImageToGaleryCreate( APIView ) :
    
    def get_object( self, pk ) :
        """
        Get object function
        """
        try :
            # Get the object by the primary key
            return Event.objects.get( pk=pk )
        except Event.DoesNotExist :
            # Return a 404 error if not found in the db
            raise Http404
    # End of get_object function
    
    def post( self, request, pk, format=None ) :
        """
        When postin the gallery image
        """
        # Get the object by primary key
        event = self.get_object( pk )
        # Get the images from the pettition
        fh = open( "imageToSave.png", "wb" )
        # Write the file
        fh.write( request.data.decode( "base64" ) )
        # Close the file
        fh.close()
        # Save the image on the competition
        save_image_to_galery( "imageToSave.png", event )
        # return the competition serialized
        return Response( EventSerializer( event ).data )
    # End of put function
# End of ImageToGaleryCreate view class