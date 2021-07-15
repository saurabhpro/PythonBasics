from django.db import models


# models.py to define the data we want to manage in our app.
# Create your models here.

# a model is just a class; it has attributes
# and methods, just like every class we’ve discussed.


class Topic(models.Model):
    """A topic the user is learning about."""
    """You use CharField when you want to store a small amount of text, such as a name, a title, or a city"""
    text = models.CharField(max_length=200)

    """to automatically set this attribute to the current date and time whenever the user creates a new topic."""
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    """kind of field doesn’t need a size limit, because we don’t want to limit the size of individual entries."""
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        it allows us to set a special
        attribute telling Django to use Entries when it needs to refer to more than
        one entry. Without this, Django would refer to multiple entries as Entrys.
        """
        verbose_name_plural = 'entries'

    # __str__() method tells Django which information to show when it refers to individual entries.
    def __str__(self):
        """Return a string representation of the model limiting length to 50 chars."""
        return f'{self.text[:50]}...'


class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)
