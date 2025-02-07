from django import template
from django.core.cache import cache

register = template.Library()

@register.filter
def is_poster(user):
    if not user.is_authenticated:
        return False

    cache_key = f"is_poster_{user.id}"
    result = cache.get(cache_key)

    # キャッシュに情報がない場合
    if result is None:
        result = user.groups.filter(name='Poster').exists()
        cache.set(cache_key, result, 3600)  # キャッシュ時間を3600秒（1時間）に設定

    return result
  
@register.filter
def is_premium(user):
    return user.groups.filter(name='Premium').exists()

@register.filter
def is_master(user):
    return user.groups.filter(name='Master').exists()

@register.simple_tag
def get_attr(obj, attr_name):
    return getattr(obj, attr_name, None)

@register.filter(name='truncatechars_custom')
def truncatechars_custom(value, arg):
    """
    Truncates a string after a certain number of characters, 
    and appends an ellipsis ('...').
    """
    try:
        length = int(arg)
    except ValueError:  # invalid literal for int()
        return value  # Fail silently
    if len(value) > length:
        value = value[:length-3]  # -3 to account for the length of the '...'
        return value + '...'
    return value