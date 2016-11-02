from django.db import models

# Create your models here.

from shortener.models import KirrURL


class ClickEventManager(models.Manager):
    def create_event(self, KirrInstance):
        if isinstance(KirrInstance, KirrURL):
            obj, created = self.get_or_create(kirr_url=KirrInstance)
            # why self.get_or_create works here because it is replacing ClickEvent.objects
            # in ClickEvent ' objects = ClickEventManager()', objects is calling ClickEventManager
            obj.count += 1
            obj.save()
            return obj.count
        return None

class ClickEvent(models.Model):
    kirr_url = models.OneToOneField(KirrURL)   #associates two models
    count = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True) #everytime when model is last saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model was created

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)