""" this docstring will silence the warning """
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
import json
import datetime
from .models import Jobseeker

# Create your views here.
def index(request):
    """ default route view """
    return HttpResponse("Hello, world. This is jobseeker country")

def detail(request, jskId):
    """ basic jobseeker objects """
    jskModel = get_object_or_404(Jobseeker, pk=jskId)
    jobseeker = model_to_dict(jskModel)
    return HttpResponse(json.dumps(jobseeker, default=datetime_handler))

def datetime_handler(val):
    if isinstance(val, datetime.datetime):
        return val.isoformat()
    if isinstance(val, datetime.date):
        return val.isoformat()
    raise TypeError("Unknown type")


