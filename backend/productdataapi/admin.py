# -*- coding: utf-8 -*-
"""
Admin views to update the models using the built in admin funciont
"""
from __future__ import unicode_literals

from django.contrib import admin

from productdataapi.models import ProductData


admin.site.register(ProductData)
