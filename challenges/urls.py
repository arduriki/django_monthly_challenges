# all the urls supported
from django.urls import path
# import views.py functions
from . import views

urlpatterns = [
    path("", views.index),  # /challenges/
    # int or str to specify which value should enter.
    path("<int:month>", views.monthly_challenge_by_number),
    # give a name to the url to construct paths
    path("<str:month>", views.monthly_challenge, name="month-challenge")  # name parameter added
]
