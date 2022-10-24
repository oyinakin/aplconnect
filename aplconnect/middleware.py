from datetime import datetime
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin

class SessionExpiredMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response
    def process_request(self, request):
        last_activity = datetime.strptime(ls, '%Y-%m-%dT%H:%M:%S.%f')
        now = datetime.strptime(datetime.now().strftime('%d/%m/%y %H:%M'),'%d/%m/%y %H:%M')
        print("last_activity is ")
        print(last_activity)
        if int(str(now-last_activity).split(":",2)[1]) > 1:
            # Do logout / expire session
            # and then...
            try:
                del request.session['user']
            except KeyError:
                print("del issue")
                pass
            logout(request)
            return HttpResponseRedirect('signin', {'error_message': "You are signed out"})
    

        if not request.is_ajax():
            # don't set this for ajax requests or else your
            # expired session checks will keep the session from
            # expiring :)
            request.session['last_activity'] = json.dumps(datetime.now(), sort_keys=True, indent=1, cls=DjangoJSONEncoder)
        print("done dat")
        return JsonResponse({"status":"OK"}) 