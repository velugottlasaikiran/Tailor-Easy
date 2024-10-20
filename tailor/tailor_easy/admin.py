from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('s_no', 'name', 'phone_number', 'date_time', 'shirt', 'pant', 'kurtha', 'others', 'shirt_cost', 'pant_cost', 'total_cost', 'advance', 'balance')

# Register your models here.
