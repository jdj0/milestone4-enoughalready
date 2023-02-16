from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserAccount(models.Model):
    """ A model for accounts that stores order history and shipping info """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20,
                                            null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80,
                                               null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40,
                                            null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_country = CountryField(blank_label="Country",
                                   null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_update_account(sender, instance, created, **kwargs):
    """ XX """
    if created:
        UserAccount.objects.create(user=instance)
    instance.useraccount.save()
