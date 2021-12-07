from django.db import models


class PromoCode(models.Model):

    code = models.CharField(max_length=100, blank=False)
    percent_off = models.IntegerField(blank=False)
    usages = models.IntegerField(blank=False, default=0)
    max_usages = models.IntegerField(blank=True, null=True)
