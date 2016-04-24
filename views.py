from django.shortcuts import render
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import date
from .models import Event, Competition, Galery, Price
from competitors.models import Register, Competitor
import os, json
from django.core.urlresolvers import reverse

def index( request ):
    """ index view """
    # Get the contents
    json_data = open( os.path.join( settings.BASE_DIR, 'static_pro', 'resources', 'general_resources.json') )
    # Get all the events from the last 3 months
    events = Event.objects.filter(date_start__lte = date.today()).order_by('-date_start')
    next_events = Event.objects.filter(date_start__gte = date.today()).order_by('date_start')[:3]
    # Put all the important variables on a context to send to the tiemplate 
    last_events_results = events[:8]
    menu_actives = [ "active", "", "", "", "" ]
    #Context variable, is just fucking important, believe it
    context = {
        'title' : '',
        'menu_actives' : menu_actives,
        'events' : events,
        'num_competitions' : Competition.objects.all().count(),
        'num_competitors' : Competitor.objects.all().count(),
        'num_events' : Event.objects.all().count(),
        'next_events' : next_events,
        "last_events_results" : last_events_results,
        'content' : json.load(json_data)['content_es']
    }# End of contex variable
    # Render the view
    return render( request, "Home/index.html", context )
# End of index view function

def contact( request ):
    """ contact view """
    # Get the contents
    json_data = open( os.path.join( settings.BASE_DIR, 'static_pro', 'resources', 'general_resources.json') )
    menu_actives = [ "", "", "", "", "active" ]
    #Context variable, is just fucking important, believe it
    context = {
        'menu_actives' : menu_actives,
        'content' : json.load(json_data)['content_es']
    }# End of contex variable
    # Render the view
    return render( request, "Home/contact.html", context )
# End of index view function

def about( request ):
    """ about view """
    # Get the contents
    json_data = open( os.path.join( settings.BASE_DIR, 'static_pro', 'resources', 'general_resources.json') )
    menu_actives = [ "", "", "", "active", "" ]
    #Context variable, is just fucking important, believe it
    context = {
        'menu_actives' : menu_actives,
        'content' : json.load(json_data)['content_es']
    }# End of contex variable
    # Render the view
    return render( request, "Home/about.html", context )
# End of index view function

def event_detail( request, pk ) :
    """
    Detail event view controller
    """
    # Get the contents
    json_data = open( os.path.join( settings.BASE_DIR, 'static_pro', 'resources', 'general_resources.json') )
    menu_actives = [ "", "active", "", "", "" ]
    # Get the event by the id ak pk
    event = Event.objects.get( pk = pk )
    context = {
        'menu_actives' : menu_actives,
        'event' : event,
        'content' : json.load(json_data)['content_es'],
        
    }# End of context variable event
    # Render the view
    return render( request, "Events/Detail.html", context )
# End of detail view controller function

def result_detail( request, pk ) :
    """
    Detail result view controller
    """
    # Get the contents
    json_data = open( os.path.join( settings.BASE_DIR, 'static_pro', 'resources', 'general_resources.json') )
    # Get the event by the id ak pk
    event = Event.objects.get( pk = pk )
    #put_galery_to_event
    menu_actives = [ "", "", "active", "", "" ]
    # context variable
    context = {
        'menu_actives' : menu_actives,
        'event' : event,
        'content' : json.load(json_data)['content_es']
    }# End of context variable event
    if event.date_start == date.today() :
        reverse("views.event.detail", pk)
    
    # Render the view
    return render( request, "Events/result_detail.html", context )
# End of detail view controller function

def competiton_detail( request, pk ) :
    """
    Detail competition view controller
    """
    # Get the contents
    json_data = open( os.path.join( settings.BASE_DIR, 'static_pro', 'resources', 'general_resources.json') )
    # Get the competition by primary key
    competition = Competition.objects.get( pk = pk )
    # The context variable for sending data to the template
    context = {
        'competition' : competition,
        'content' : json.load(json_data)['content_es']   
    }# End of context variable competition
    # Render the view
    return render( request, "Competitions/Detail.html", context )
# End of competition detail view controller function

def result_list( request ) :
    """
    Result list view
    This will return the events that has resutls 
    """
    # Get the contents
    json_data = open( os.path.join( settings.BASE_DIR, 'static_pro', 'resources', 'general_resources.json') )
    # Get all the events
    event_list = Event.objects.filter( date_start__lte = date.today() ).order_by('-date_start')
    # Initi
    paginator = Paginator( event_list, 12 )
    #initialize the page variable if the request has a page variable
    page = request.GET.get( 'page' )
    #Verify the paginations
    try :
        events = paginator.page( page )
    except PageNotAnInteger :
        # If page is not an integer, deliver first page.
        events = paginator.page( 1 )
    except EmptyPage :
        # If page is out of range (e.g. 9999), deliver last page of results.
        events = paginator.page( paginator.num_pages )
    # Init the context variable
    context = {
        'menu_actives' : [ "", "", "active", "", "" ],
        'events' : events,
        'content' : json.load(json_data)['content_es']
    }# End of context variable
    # render the view
    return render( request, 'Events/results.html', context )
# End of result_list view controller function 

def event_index( request ) :
    """
    Event index
    This will return all the events on the template; all!
    """
    # Get the contents
    json_data = open( os.path.join( settings.BASE_DIR, 'static_pro', 'resources', 'general_resources.json') )
    # Get all the events
    event_list = Event.objects.all().order_by('-date_start')
    # The next events
    next_events = Event.objects.filter(date_start__gte = date.today()).order_by('date_start')
    # Initi
    paginator = Paginator( event_list, 12 )
    #initialize the page variable if the request has a page variable
    page = request.GET.get( 'page' )
    #Verify the paginations
    try :
        events = paginator.page( page )
    except PageNotAnInteger :
        # If page is not an integer, deliver first page.
        events = paginator.page( 1 )
    except EmptyPage :
        # If page is out of range (e.g. 9999), deliver last page of results.
        events = paginator.page( paginator.num_pages )
    # Init the context variable
    context = {
        'menu_actives' : [ "", "active", "", "", "" ],
        'next_events' : next_events,
        'events' : events,
        'content' : json.load(json_data)['content_es']  
    }# End of context variable
    # Render the view
    return render( request, 'Events/index.html', context )
# End of event_index function

def search_results( request, pk ):
    """
    Get function just for getting the fucking register number
    """
    context = {}
    # First get the competition by primary key
    # Get the event by competition 
    event = Event.objects.get( pk = pk )
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
        # Context variable    
        context = {
            "registers" : registers
        }
        # Return the last number plus one, the puls one is on the data encaps
        return render( request, 'Events/search_results.html', context )
    # If there is no register return 1
    # render the view
    return render( request, 'Events/search_results.html', context )
# End of search_results function

def put_all_images () :
    """
    put all images
    This function is just for hardcoding the images on the event table
    """
    # Get all the events    
    events = Event.objects.all()
    # url 
    img_url = "http://i.imgur.com/K9BJXgA.jpg"
    # Loops
    for e in events :
        # Set the image url
        e.image_url = img_url
        # Save the model
        e.save()
    # End of loop
# End of put_all_images function

def put_galery_to_event( event_id ) :
    """
    Puts a bunch of images to the galery model
    """
    # Get the event
    event = Event.objects.get( pk = event_id )
    # Set the image url variable
    img_url = "http://i.imgur.com/K9BJXgA.jpg"
    # put four galery models
    for i in range( 1, 3 ):
        galery = Galery()
        galery.event = event
        galery.image_url = img_url
        galery.save()
    # End of loop
# End of put_galery_to_event function