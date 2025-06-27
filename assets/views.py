from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta

from .models import Asset, Notification, Violation
from .serializers import AssetSerializer

class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

@api_view(['GET'])
def run_checks(request):
    now = timezone.now()
    upcoming = now + timedelta(minutes=15)
    assets = Asset.objects.all()

    for asset in assets:
        if now < asset.service_time <= upcoming:
            Notification.objects.get_or_create(asset=asset, type='service')

    
        if now < asset.expiration_time <= upcoming:
            Notification.objects.get_or_create(asset=asset, type='expiration')
        if asset.service_time < now and not asset.is_serviced:
            Violation.objects.get_or_create(asset=asset, issue='Service overdue')
        if asset.expiration_time < now:
            Violation.objects.get_or_create(asset=asset, issue='Asset expired')

    return Response({'message': 'Check completed'})

