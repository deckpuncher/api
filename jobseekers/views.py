""" this docstring will silence the warning """
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from django.core import serializers
import json
import datetime
from .models import Jobseeker, Profile
from django.core.exceptions import ValidationError, NON_FIELD_ERRORS
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def jobseekers(request):
    """ default route, list all records """
    if (request.method == 'GET'):
        jsk_list = list(Jobseeker.objects.all().values('JobseekerId'))
        return JsonResponse(jsk_list, json_dumps_params={'indent':4}, safe=False)
    if (request.method == 'POST'):
        newJsk = json.loads(request.body.decode("utf-8"), object_hook=jobseeker_builder)

        try:
            newJsk.full_clean()
        except ValidationError as e:
            non_field_errors = e.message_dict[NON_FIELD_ERRORS]
            print(non_field_errors)
            return JsonResponse(non_field_errors, status=400, safe=False)
        newJsk.save()

        return JsonResponse(model_to_dict(newJsk), json_dumps_params={'indent':4}, status=201)

def jobseekerDetail(request, jskId):
    """ basic jobseeker objects """
    jskModel = get_object_or_404(Jobseeker, pk=jskId)
    jobseeker = model_to_dict(jskModel)
    return JsonResponse(jobseeker, json_dumps_params={'indent':4})

def profiles(request, jskId):
    """ basic jobseeker objects """   
    profModel = get_object_or_404(Profile, jobseeker=jskId)
    profile = model_to_dict(profModel)
    return JsonResponse(profile, json_dumps_params={'indent':4})

# dont need this for JsonResponse
def date_handler(val):
    if hasattr(val, 'isoformat'):
        return val.isoformat()

def jobseeker_builder(obj):
    return Jobseeker(JobseekerId=obj['JobseekerId'],
                     FirstName=obj['FirstName'],
                     LastName=obj['LastName'],
                     Email=obj['Email'],
                     DOB=obj['DOB'])
