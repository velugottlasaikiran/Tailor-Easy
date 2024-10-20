from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = [
            's_no', 'date_time', 'name', 'phone_number', 'shirt', 'pant', 
            'kurtha', 'others', 'shirt_cost', 'pant_cost', 'total_cost', 
            'advance', 'balance', 'customer_image', 'shirt_image', 'pant_image'
        ]