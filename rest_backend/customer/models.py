from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, related_name='customer', on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    age = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username

    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Customer.objects.create(user=instance)
    # post_save.connect(create_user_profile, sender=User)

    # def save_user_profile(sender, instance, **kwargs):
    #     instance.customer.save()
    # post_save.connect(save_user_profile, sender=User)
