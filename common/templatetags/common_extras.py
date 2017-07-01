from django import template

register = template.Library()


@register.filter
def type_of(value):
    return type(value)


@register.filter
def show_dir(value):
    print(dir(value))
    return value