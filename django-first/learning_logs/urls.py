"""Defines URL patterns for learning_logs."""
from django.urls import path

# the dot tells Python to import the views.py module from the same directory as  the current urls.py module.
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    # Django receives the requested URL and tries
    # to route the request to a view. It does this by searching all the URL patterns
    # we’ve defined to find one that matches the current request. Django ignores
    # the base URL for the project (http://localhost:8000/), so the empty string
    # ('') matches the base URL. Any other URL won’t match this pattern, and
    # Django will return an error page if the URL requested doesn’t match any
    # existing URL patterns.
    path('', views.index, name='index'),

    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic. The part /<int:topic_id>/,
    # matches an integer between two forward slashes and stores the integer
    # value in an argument called topic_id.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]
