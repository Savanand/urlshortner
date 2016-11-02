"""kirr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

# from shortener.views import kirr_redirect_FBV, KirrRedirectCBView, test_view  # for Django 1.10 this is required

from shortener.views import HomeView, KirrRedirectCBView

# DO NOT USE LIKE THIS BELOW with like as older DJANGO versions
# from shortener import views
# from another_app.views import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView.as_view()),

    # url(r'^about123/$', test_view),
    # url(r'^(?P<shortcode>[\w-]+){6,15}$', kirr_redirect_FBV),
    url(r'^(?P<shortcode>[\w-]+){6,15}/$', KirrRedirectCBView.as_view()),
        # refer https://github.com/codingforentrepreneurs/Guides/blob/master/all/common_url_regex.md

    # DO NOT USE LIKE THIS BELOW with like as older DJANGO versions
    # url(r'^view-2/$', 'shortener.views.KirrRedirectCBView'),
    # url(r'^view-2/$', views.KirrRedirectCBView),
]
