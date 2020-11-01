from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter
def list_index(row, i):
    try:
        return row[i]
    except IndexError:
        return ''


@register.filter
def update_radio_value(whole_radio_tag:list, received_change):
    #not in use
    beginning = whole_radio_tag[:45]
    middle = whole_radio_tag[45] + '_' + str(received_change)
    end = whole_radio_tag[46:]
    new_radio_tag = beginning + middle + end
    try:    
        return mark_safe(new_radio_tag)
    except IndexError:
        return ''