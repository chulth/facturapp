# -*- coding: utf-8 -*-
"""
Database models for productdataapi.
"""

from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from productdataapi.models import ProductData, BillRegistration


class ProductDataSerializer(serializers.ModelSerializer):
    """
    A simple serializer for our ProductData model
    """
    id = serializers.ReadOnlyField() 
    name = serializers.CharField(max_length=100)
    value = serializers.CharField(max_length=20) 

    class Meta:
        model = ProductData
        fields = ["id","name","value"]

class BillRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillRegistration
        fields = ['id_bill', 'products', 'total_price']
    
    def create(self, data, **kwargs):
        bill = BillRegistration.objects.create(**data)

