from django.contrib import admin
from .forms import EventForm, EventTypeForm, CompetitionTypeForm, CompetitionForm, PriceForm, CategoryForm
from .models import Event, EventType, CompetitionType, Competition, Price, Category

# Register your models here.

"""
Event admin
"""
class EventAdmin( admin.ModelAdmin ) :
    form = EventForm
    list_display = [
        "__unicode__",
        "name",
        "date_start",
        "date_finish",
        "event_type",
    ]
# End of Event Admin class

"""
Event type form 
"""
class EventTypeAdmin( admin.ModelAdmin ) :
    form = EventTypeForm
    list_display = [
        "__unicode__",
        "timestamp",
        "updated",
    ]
# End of EventTypeAdmin class

"""
Copmetition type admin
"""
class CompetitionTypeAdmin( admin.ModelAdmin ) :
    form = CompetitionTypeForm
    list_display =  [
        'id',
        'name',
        'description',    
    ]
# End of competition type admin

class CompetitionAdmin( admin.ModelAdmin ) :
    form = CompetitionForm
    list_display = [
        'name',
        'description',
        'date_start',
        'competition_event',
        'cost',
    ]
# End of competition admin class

"""
Price admin
"""
class PriceAdmin( admin.ModelAdmin ) :
    form = PriceForm
    list_display = [
        'name',
        'description',
        'event',    
    ]
# End of price admin class

"""
Category class
"""
class CategoryAdmin( admin.ModelAdmin ) :
    form = CategoryForm
    list_display = [
        'name',
        'description',
        'age_1',
        'age_2',
    ]
# End of category admin class

admin.site.register( Event, EventAdmin )
admin.site.register( EventType, EventTypeAdmin )
admin.site.register( CompetitionType, CompetitionTypeAdmin )
admin.site.register( Competition, CompetitionAdmin )
admin.site.register( Price, PriceAdmin )
admin.site.register( Category, CategoryAdmin )