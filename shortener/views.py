from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .forms import SubmitUrlForm
from .models import KirrURL


def home_view_fbv(request, *args, **kwargs):  # fbv for home just for if
    if request.method == "POST":
        print (request.method)
    return render(request, "shortener/home.html", {})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title" : "Kirr.co",
            "form" : the_form,
        }
        return render(request, "shortener/home.html", context)  #find ref at 1.8 project

    def post(self, request, *args, **kwargs):
     #    some_dict = {}
     # #   some_dict['url'] #error
     #    some_dict.get('url', 'http://www.google.com') #if none
     #    print (request.POST)
     #    print (request.POST["url"])
     #    print (request.POST.get("url"))
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Kirr.co",
            "form": form,
        }

        template = "shortener/home.html"
        if form.is_valid():
            # print ("in post method")
            # print(form.cleaned_data)
            new_url = form.cleaned_data.get("url")
            obj, created = KirrURL.objects.get_or_create(url=new_url)
            context = {
                "object" : obj,
                "created" : created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return  render(request, template, context)

class URLRedirectView(View):  #class based view  you've to explicity write method you want to call
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrURL, shortcode=shortcode)
        # print ('Url=',obj.url)
        print ("in URLRedirectView ", ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)


# # Create your views here.
# def test_view(requst, shortcode=None, *args, **kwargs):
#     return HttpResponse("Some about response")
#
# def kirr_redirect_FBV(request, shortcode=None, *args, **kwargs): # function based view
#     obj = get_object_or_404(KirrURL, shortcode=shortcode)
#     print ('Url=',obj.url)
#     return HttpResponseRedirect(obj.url)


    # def post(self, request, *args, **kwargs):
    #     return HttpResponse()
    #

'''
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
'''