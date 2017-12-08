from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response

from api.models import About, SNS, Product, Inquiry
from api.serializers import AboutSerializer


class AboutGetView(generics.ListAPIView):

    def get(self, request):
        query = About.objects.all()
        serializer = AboutSerializer(query)

        return Response(serializer.data, status=status.HTTP_200_OK)
