# -*- coding: utf-8 -*-
"""
URLs for productdataapi.
"""
from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from productdataapi.views import ProductDataViewSet, BillRegistrationViewSet

ROUTER = DefaultRouter()
ROUTER.register(r'productdata', ProductDataViewSet)
ROUTER.register(r'billregistration', BillRegistrationViewSet)

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'api/v1/', include(ROUTER.urls)),
    path(r'', TemplateView.as_view(template_name="productdataapi/base.html")),
]
