# -*- coding: utf-8 -*-
"""
Views for productdataapi.
"""

from __future__ import absolute_import, unicode_literals

from rest_framework import viewsets, permissions
import json
import logging
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from productdataapi.models import ProductData, BillRegistration
from productdataapi.serializers import (
    ProductDataSerializer, BillRegistrationSerializer)

class ProductDataViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving ProductData.
    """

    queryset = ProductData.objects.all()
    serializer_class = ProductDataSerializer
    permission_classes = (permissions.AllowAny,)


class BillRegistrationViewSet(viewsets.ModelViewSet):    
    """
    ViewSet for bill registration.
    """

    serializer_class = BillRegistrationSerializer
    queryset = BillRegistration.objects.all()
    permission_classes = (permissions.AllowAny,)


    # @action(detail=True, methods=['post'])
    def create(self, request):
        data =json.loads(request.body)
        print(data)
        products = data.get("products")
        total = 0
        try:
            if not products:
                raise BaseException("This bill does not have any products")
            for value in products:
                total = total + int(value.get("value"))

            if data.get("codigo") == "Promo_Platzi":
                total = _caltulate_total_with_discount(total)
            bill = BillRegistration.objects.create(
                products=products,total_price=str(total))
            print(bill)
            return Response(bill.total_price)
        except BaseException as e:
            logging.exception(e)
            return Response(status=status.HTTP_204_NO_CONTENT)
        
def  _caltulate_total_with_discount(amount):
    discount = amount * 0.30
    return  amount - discount 