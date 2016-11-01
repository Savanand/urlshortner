from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View


from .models import KirrURL


# Create your views here.
def kirr_redirect_FBV(request, shortcode=None, *args, **kwargs): # function based view
    # print(request.user, request.user.is_authenticated())
    # print(args, kwargs)
    # print (shortcode)

    print ('method is',request.method)
    obj = get_object_or_404(KirrURL, shortcode=shortcode)
    # obj_url = obj.url
    # try:
    #     obj = KirrURL.objects.get(shortcode=shortcode)
    # except:
    #     obj = KirrURL.objects.all().first()

    # obj_url = None
    # qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
    # if qs.exists() and qs.count() == 1:
    #     obj = qs.first()
    #     obj_url = obj.url

    # return HttpResponse("Hello from kirr_redirect_view- Hello shortcode {sc}".format(sc= shortcode))
    return HttpResponse("Hello shortcode {sc}".format(sc=obj.url))


class KirrRedirectCBView(View):  #class based view  you've to explicity write method you want to call
    def get(self, request, shortcode=None, *args, **kwargs):
        # print(request.user, request.user.is_authenticated())
        # print(args, kwargs)
        # print (shortcode)
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        return HttpResponse("Hello again from KirrRedirectView- Hello shortcode {sc}".format(sc= shortcode))

    def post(self, request, *args, **kwargs):
        return HttpResponse()