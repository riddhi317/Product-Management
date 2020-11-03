from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext as _
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(_(u"Name"), max_length=250)
    sub_category = models.ForeignKey(
        "self", blank=True, null=True, related_name="+", on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Product(TimeStampedModel):
    """ This Model is for Product ,here you can add Product name which you want."""
    name = models.CharField(max_length=30, null=True)
    product_code = models.CharField(max_length=30, null=True)
    price = models.FloatField(max_length=30, null=True)
    category = models.ForeignKey("Category", verbose_name=_(
        u"Category"), blank=True, null=True, related_name="+", on_delete=models.CASCADE)
    manufacture_date = models.DateTimeField(null=True)
    expiry_date = models.DateTimeField(null=True)
    product_owner = models.ForeignKey(User,on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
