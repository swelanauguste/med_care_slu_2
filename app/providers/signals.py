from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (
    Address,
    Contact,
    Education,
    ImmunisationStatement,
    NextOfKin,
    OtherDetail,
    Provider,
    WorkInterest,
)


@receiver(post_save, sender=Provider)
def create_provider_profile(sender, instance, created, **kwargs):
    if created:
        Address.objects.create(provider=instance)
        Contact.objects.create(provider=instance)
        Education.objects.create(provider=instance)
        ImmunisationStatement.objects.create(provider=instance)
        NextOfKin.objects.create(provider=instance)
        OtherDetail.objects.create(provider=instance)
        WorkInterest.objects.create(provider=instance)


@receiver(post_save, sender=Provider)
def save_provider_profile(sender, instance, **kwargs):
    instance.provider.save()
    # instance.contact.save()
    # instance.education.save()
    # instance.immunisationstatement.save()
    # instance.nextofkin.save()
    # instance.otherdetail.save()
    # instance.workinterest.save()
