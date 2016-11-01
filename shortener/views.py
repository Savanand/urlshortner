from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def kirr_redirect_FBV(request, shortcode=None, *args, **kwargs): # function based view
    # print(request.user, request.user.is_authenticated())
    # print(args, kwargs)
    print (shortcode)
    return HttpResponse("Hello from kirr_redirect_view- Hello shortcode {sc}".format(sc= shortcode))

class KirrRedirectCBView(View):  #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        # print(request.user, request.user.is_authenticated())
        # print(args, kwargs)
        print (shortcode)
        return HttpResponse("Hello again from KirrRedirectView- Hello shortcode {sc}".format(sc= shortcode))

