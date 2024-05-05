from django.shortcuts import render
# import the httpresponse
from django.http import HttpResponse

# Create your views here.


def index(request):
    """Return a response to the client's request."""
    # return an instantiated imported class
    # as an argument, give back something: a html for example.
    return HttpResponse("This works!")
