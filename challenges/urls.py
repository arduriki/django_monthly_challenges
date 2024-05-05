# all the urls supported
from django.urls import path
# import views.py functions
from . import views

urlpatterns = [
    # first argument: string that describes the url to be supported.
    # second argument: pointer at the view function.
    path("january", views.index)
    # URL configured and which view to be executed.
]
