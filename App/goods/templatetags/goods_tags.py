from django import template
from django.http.request import urlencode
from goods.models import Categories

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs) -> str:
    query: Any = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
