# custom_tags.py

# from django import template
# from django.utils import timezone

# register = template.Library()

# @register.filter
# def is_edit_allowed(datetime_value):
#     # Assuming datetime_value is timezone-aware
#     current_datetime = timezone.now()
    
#     # Check if the input datetime is in the future, allowing edits
#     return datetime_value > current_datetime





# custom_tags.py

from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def is_edit_allowed(datetime_value):
    # Assuming datetime_value is timezone-aware
    current_datetime = timezone.now()

    # Calculate the minimum allowed datetime (3 hours difference)
    min_allowed_datetime = datetime_value + timezone.timedelta(minutes=120)
    # print("min_allowed_datetime", min_allowed_datetime)
    # print("datetime_value", datetime_value)
    # Check if the input datetime is after the minimum allowed datetime, allowing edits
    return current_datetime > min_allowed_datetime
