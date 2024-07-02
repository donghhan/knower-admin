from django import template

register = template.Library()


# Array spliting
@register.filter(name="split")
def split(value):
    return value.split("/")


# Check if string word includes specific word
@register.filter(name="includes")
def includes(value, arg):
    return value.find(arg)
