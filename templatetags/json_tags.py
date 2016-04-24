from django.core.serializers import serialize
from django.db.models.query import QuerySet
try:
    from django.utils import simplejson as json
except:
    import simplejson as json
from django.template import Library

register = Library()

def jsonify(object):
    """
    Filter for stringify a query set from the template
    """
    # Validate if the object sended is a queryset type
    if isinstance(object, QuerySet) :
        # Return serialized object on utf8 decode
        return serialize('json', object).encode('utf8')
    # Return the sample json
    return simplejson.dumps(object, ensure_ascii=False).encode('utf8')
# register the filter
register.filter('jsonify', jsonify)