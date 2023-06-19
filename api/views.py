from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import permissions


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def ad_list(request):
    if request.method == 'GET':
        ad = Advertisement.objects.all()
        serializer = AdvertisementSerializer(ad, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def ad_detail(request, pk):
    try:
        ad = Advertisement.objects.get(pk=pk)
    except Advertisement.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdvertisementSerializer(ad)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdvertisementSerializer(ad, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Schedule
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def adCampaign_list(request):
    if request.method == 'GET':
        adCampaign = AdCampaigns.objects.all()
        serializer = AdCampaignSerializer(adCampaign, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdCampaignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def adCampaign_detail(request, pk):
    try:
        adCampaign = AdCampaigns.objects.get(pk=pk)
    except AdCampaigns.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdCampaignSerializer(adCampaign)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdCampaignSerializer(adCampaign, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        adCampaign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


#role
@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def adImpresssion_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        adImpresssion = AdImpresssions.objects.all()
        serializer = AdImpresssionSerializer(adImpresssion, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdImpresssionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.AllowAny,))
def adImpresssion_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        adImpresssion = AdImpresssions.objects.get(pk=pk)
    except AdImpresssions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdImpresssionSerializer(adImpresssion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AdImpresssionSerializer(adImpresssion, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        adImpresssion.delete()
        return Response({
            status:status.HTTP_204_NO_CONTENT
        })


