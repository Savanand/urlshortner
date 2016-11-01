from django.db import models
# Create your models here.
from .utils import code_generator, create_shortcode


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
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True, blank=True)
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
        super(KirrURL, self).save(*args, **kwargs)


    # class Meta:
    #   ordering = '-id'
    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)