from django.shortcuts import redirect
from potatoesathome import settings

class AuthRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if request.path_info not in ['/login/','/signup/'] and '/activate/' not in request.path_info:
            if not request.user.is_authenticated:
                return redirect('%s?next=%s' % (settings.LOGIN_path, request.path))

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.

        return response