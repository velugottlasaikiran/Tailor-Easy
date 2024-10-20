
# Create your models here.

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 
    s_no = models.AutoField(primary_key=True) 
    date_time = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    shirt = models.CharField(max_length=255, blank=True, null=True)
    pant = models.CharField(max_length=255, blank=True, null=True)
    kurtha = models.CharField(max_length=255, blank=True, null=True)
    others = models.CharField(max_length=255, blank=True, null=True)
    shirt_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pant_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    advance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    customer_image = models.ImageField(upload_to='customer_images/', blank=True, null=True)
    shirt_image = models.ImageField(upload_to='shirt_images/', blank=True, null=True)
    pant_image = models.ImageField(upload_to='pant_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email