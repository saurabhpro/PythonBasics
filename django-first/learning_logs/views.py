from django.shortcuts import render

from .models import Topic


# Create your views here.
# A view function takes in information from a request, prepares the data
# needed to generate a page, and then sends the data back to the browser,
# often by using a template that defines what the page will look like.

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics.
    We query the database by asking for the Topic objects, sorted by the date_added attribute.
    """
    topics = Topic.objects.order_by('date_added')
    print(topics)

    # context is a dictionary in which the keys are names we’ll use in the template to access
    # the data, and the values are the data we need to send to the template.
    context = {'topics': topics}

    return render(request, 'learning_logs/topics.html', context)


# When you’re writing queries like these in your own projects, it’s
# helpful to try them out in the Django shell first.
def topic(request, topic_id):
    """Show a single topic, and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
