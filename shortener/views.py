from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
def kirr_redirect_FBV(request, *args, **kwargs): # function based view
    return HttpResponse("Hello from kirr_redirect_view")

class KirrRedirectCBView(View):  #class based view
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello again from KirrRedirectView")

