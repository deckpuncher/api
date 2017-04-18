""" this docstring will silence the warning """
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
import json
import datetime
from .models import Jobseeker

# Create your views here.
def index(request):
    """ default route, list all records """
    jsk_list = list(Jobseeker.objects.all())
    return HttpResponse(json.dumps(jsk_list, default=datetime_handler))

def detail(request, jskId):
    """ basic jobseeker objects """
    jskModel = get_object_or_404(Jobseeker, pk=jskId)
    jobseeker = model_to_dict(jskModel)
    return HttpResponse(json.dumps(jobseeker, default=datetime_handler))

def datetime_handler(self, val):
    if hasattr(val, 'isoformat'):
        return val.isoformat()
    else:
        return json.JSONEncoder.default(self, val)
        