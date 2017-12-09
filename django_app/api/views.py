from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import viewsets

from api.models import About, SNS, Product, Inquiry
from api.serializers import AboutSerializer, SNSSerializer


class AboutGetView(generics.ListAPIView):

    def get(self, request):
        query = About.objects.all()
        serializer = AboutSerializer(query)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SNSGetView(viewsets.ViewSet):

    def list(self, request):
        query = SNS.objects.all()
        serializer = SNSSerializer(query)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, name):
        query = get_object_or_404(SNS, name=name)
        serializer = AboutSerializer(query)

        return Response(serializer.data, status=status.HTTP_200_OK)
