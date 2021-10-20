# -*- coding: utf-8 -*-
"""
Database models for productdataapi.
"""

from __future__ import absolute_import, unicode_literals

import collections
import uuid
import jsonfield

from django.db import models


class ProductData(models.Model):
    """
    Model to store our Product data
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # pylint: disable=invalid-name
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class BillRegistration(models.Model):
    """
    Model to store our bill registration information
    """
    id_bill = models.UUIDField(
        primary_key=True, default=uuid.uuid4,editable=False)
    products = jsonfield.JSONField(
        blank=True,
        null=True, 
        load_kwargs={'object_pairs_hook': collections.OrderedDict})
    total_price = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.id_bill)





models.ManyToManyField(ProductData)