from .models import Sessions
mng = Sessions.manager

class Sessioner:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self,request,func,*view_args,**view_kwargs):
        deleted = mng.delete_if_expired(request) #deletes cookie from db if expired.
        if not deleted:
            mng.refresh_expr(request)      #if session is not expired and client send request to server
                                           #refreshes its expiration time.current time + 60 minutes.
                                           #60 minutes can be changed via settings.py.(COOKIE_LIFE)
