from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import pre_save,post_save
from .models import filecompare
from .views import logging 
logger = logging.getLogger('django')




@receiver(post_save, sender=filecompare)
def my_callback(sender, instance,**kwargs):
    logger.info("#######################Running required file modifed content####################")
    logger.info("###############################################################################")
    print("Request finished!")
    print(instance)