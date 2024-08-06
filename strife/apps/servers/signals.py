from django.dispatch import receiver
from django.db.models.signals import post_delete

from .models import Server


@receiver(post_delete, sender=Server)
def delete_server_owner_obj(sender, instance, *_args, **_kwargs):
    if instance.owner:
        instance.owner.delete()
