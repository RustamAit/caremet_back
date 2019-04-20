from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from helperRequestApi.models import Helper, HelperRequest
from helperRequestApi.serializers import HelperSerializer, HelperRequestSerializer


class HelperList(viewsets.ModelViewSet):
    queryset = Helper.objects.all()
    serializer_class = HelperSerializer


class HelperRequestList(viewsets.ModelViewSet):
    queryset = HelperRequest.objects.all()
    serializer_class = HelperRequestSerializer
