from django import forms
from .models import Event, EventType, Competition, Category, CompetitionType, Price, Category

"""
Event form class
"""
class EventForm( forms.ModelForm ) :
    
    """
    Meta class
    """
    class Meta :
        model = Event
        fields = [
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
        ]
    # End of Meta class
# End of Event Form class

class EventTypeForm( forms.ModelForm ) :
    
    """
    Meta class
    """
    class Meta :
        model = EventType
        fields = [
            'name',
            'description',
        ]
    # End of Meta class
# End of EventTypeForm class

class CompetitionTypeForm( forms.ModelForm ) :
    
    """
    Meta class
    """
    class Meta:
        model = CompetitionType
        fields = [
            'name',
            'description',
        ]
    # End of meta class
# End of CompetitionTypeForm class

"""
Competition form
"""
class CompetitionForm( forms.ModelForm ) :
    
    """
    Meta class
    """
    class Meta :
        model = Competition
        fields = [
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
        ]
    # End of meta class
# End of competition form class

"""
Price form class
"""
class PriceForm( forms.ModelForm ) :
    
    """
    Meta class
    """
    class Meta :
        model = Price
        fields = [
            'name',
            'description',
            'image_url',
            'event',
        ]
    # End of meta class
# End of price class

"""
Category form class
"""
class CategoryForm( forms.ModelForm ) :
    
    """
    Meta class
    """
    class Meta :
        model = Category
        fields = [
            'user',
            'name',
            'description',
            'age_1',
            'age_2',
            'color',
        ]
    # End of meta class
# End of Category Form class