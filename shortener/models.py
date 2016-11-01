from django.db import models
import random
import string
# Create your models here.

# method to generate string of random 6 characters
def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    # equivalent for loop would be
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # return new_code
    return ''.join(random.choice(chars) for _ in range(size))


class KirrURL(models.Model):
    url = models.CharField(max_length=220,)
    shortcode = models.CharField(max_length=15, unique=True)
    updated = models.DateTimeField(auto_now=True) #everytime when model is last saved
    timestamp = models.DateTimeField(auto_now_add=True) #when model was created

    #empty_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False)  # we can set our own date

    #over-riding inbuilt save method
    def save(self, *args, **kwargs):
        print ("something")
        self.shortcode = code_generator()
        super(KirrURL, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)