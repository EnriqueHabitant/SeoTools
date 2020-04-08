from django import template
from django.template.base import Variable


register = template.Library()

@register.filter(name='index')
def get_index(list_, value):
    return list_.index(value)

@register.filter(name='addstr')
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.filter(name='get_value')
def get_value(list_, list_2):
    lista = ['None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None', 'None']
    for res in list_2:
        date = res['date'].strftime("%b, %Y")
        if date in list_:
            index = list_.index(date)
            lista[index] = res['search_volume']
            
    return lista
        
@register.filter(name='ifnumbrefloat')
def ifnumbrefloat(value, n):
    if value == None:
        return 'None'
    else:
        try:
            return round(float(value), int(n))
        except ValueError:
            return Variable(value).resolve