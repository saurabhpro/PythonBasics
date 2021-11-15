from django.db import models


class Review(models.Model):
    REVIEW_APPROVAL_STATUS = (
        ('Pending', 'PENDING'),
        ('Approved', 'APPROVED'),
        ('Denied', 'DENIED'),
    )

    """Represents a review to be read from reviews csv"""
    submitted_date = models.DateTimeField()
    venue_id = models.IntegerField()
    ws_user_email_id = models.EmailField()
    overall_rating = models.IntegerField()
    review_text = models.CharField(max_length=3000)
    status = models.CharField(max_length=10)
    review_id = models.UUIDField(primary_key=True)
