from django import template

register = template.Library()


@register.filter
def calculate_date_difference(from_date, given_data):
    return from_date - given_data
