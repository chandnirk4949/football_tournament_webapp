# custom_tags.py

from django import template
from django.utils import timezone

register = template.Library()


# function to check if the score edit is allowed or not
@register.filter
def is_edit_allowed(datetime_value):
    # Assuming datetime_value is timezone-aware
    current_datetime = timezone.now()

    # Calculate the minimum allowed datetime (3 hours difference)
    min_allowed_datetime = datetime_value + timezone.timedelta(minutes=120)
    # Check if the current datetime is after the minimum allowed datetime, allowing edits
    return current_datetime > min_allowed_datetime
