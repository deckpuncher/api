""" this docstring will silence the warning """
from django.http import HttpResponse

# Create your views here.
def index(request):
    """ default route view """
    return HttpResponse("Hello, world. This is the index")
