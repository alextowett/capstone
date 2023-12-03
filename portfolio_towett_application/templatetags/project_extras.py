from django import template
register = template.Library()


@register.simple_tag
def get_project_status_info(status):
    # Define a dictionary that maps each status value to an icon URL and a background color
    status_info = {
        'designing': {
            'icon': '/static/images/designing.svg',
            'color': '#FFA000',
        },
        'developing': {
            'icon': '/static/images/developing.svg',
            'color': '#1872ba',
        },
        'testing': {
            'icon': '/static/images/testing.svg',
            'color': '#FF5D5B',
        },
        'deploying': {
            'icon': '/static/images/deploying.svg',
            'color': '#4A148C ',
        },
        'live': {
            'icon': '../static/images/live.svg',
            'color': '#388E3C',
        },
        'acquired': {
            'icon': '../static/images/acquired.svg',
            'color': '#9E9E9E',
        },
        'suspended': {
            'icon': '../static/images/suspended.svg',
            'color': '#F44336',
        },
    }

    # Return the dictionary for the given status value
    return status_info[status]
