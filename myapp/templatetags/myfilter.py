from django import template
register = template.Library()

@register.filter
def pow(co_so, so_mu):
    return co_so**so_mu

@register.filter
def make_range(number):
    return range(1,number+1)

@register.filter
def make_index_table(page,counter):
    pageginate_by=5
    return pageginate_by *(page-1) + counter