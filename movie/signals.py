from django.db.models.signals import post_save, post_delete, pre_save ,pre_delete
from django.core.mail import send_mail
from .models import Movie
from django.dispatch import receiver



@receiver(post_delete,sender=Movie)
def notify_admins(signal,sender,instance,using,**kwargs):
    print("the deleted movies is {}".format(instance))


#
# @receiver(post_save, sender=Movie)
# def my_handler(sender, instance, created, *args, **kwargs):
#     send_mail('Movie Created ', 'Dear Movie {} create'.format(instance.name),
#           'elsayedalimohamed123@gmail.com', ['elsayedali3632@gmail.com'], fail_silently=False
#           )