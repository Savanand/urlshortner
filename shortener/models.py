from django.db import models
from django.conf import settings

#from django.core.urlresolvers import reverse
from django_hosts.resolvers import reverse

# Create your models here.

from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot_com

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)


class KirrURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(KirrURLManager, self).all(*args, **kwargs)
        qs= qs_main.filter(active=True)
        return qs

    def refresh_shortcodes(self, items=None):
        print ("items to refresh in the method=", items)
        qs = KirrURL.objects.filter(id__gte=1)
        #order items in reverse
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes_count = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print (q.id, q.shortcode)  # print id and shortcodes
            q.save()
            new_codes_count += 1;
        return "new codes ready {i}".format(i=new_codes_count)


class KirrURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url, validate_dot_com])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True) #everytime when model is last saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model was created
    active = models.BooleanField(default=True)
    #empty_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False)  # we can set our own date

    objects = KirrURLManager()  #hooking up this class to its modelmanager
   # some_random = KirrURLManager()
    #over-riding inbuilt save method
    def save(self, *args, **kwargs):
        # print ("something")
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if not "http" in self.url:
            self.url = "http://" +self.url
        super(KirrURL, self).save(*args, **kwargs)


    # class Meta:
    #   ordering = '-id'
    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        print (self.shortcode)
        url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
        return url_path
