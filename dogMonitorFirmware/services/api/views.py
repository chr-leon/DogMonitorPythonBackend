from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class ServiceViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        print("here")
        return Response({},status=status.HTTP_200_OK)