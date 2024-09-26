from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def get_profile_url(user):
    # Check if the user is associated with a Staff object
    if hasattr(user, 'staff'):
        return reverse('profile')  # Assuming 'profile' is the Staff profile URL
    
    # Check if the user is associated with an Admin object
    elif hasattr(user, 'admin'):
        return reverse('admin_profile')  # Assuming 'admin_profile' is the Admin profile URL
    
    # Check if the user is associated with a ThriveAdmin object
    elif hasattr(user, 'thriveadmin'):
        return reverse('thrive_admin_profile')  # Assuming 'thrive_admin_profile' is the ThriveAdmin profile URL
    
    # Default fallback if none of the above applies
    return reverse('profile')
