from django import template
from ..models import Sessions
register = template.Library()
mng = Sessions.manager


@register.filter("is_admin")
def admin(request):
    session_key = mng.key_from_request(request)
    return mng.is_admin(session_key)

@register.filter('is_loggedin')
def loggedin(request):
    if mng.is_valid(request):
        return True
    return False