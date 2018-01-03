from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework import viewsets

from api.models import About, SNS, Product, Inquiry
from api.serializers import AboutSerializer, SNSSerializer, ProductSerializer


class AboutGetView(generics.ListAPIView):

    def get(self, request):
        query = About.objects.all()[0]
        serializer = AboutSerializer(query)

        return Response(serializer.data, status=status.HTTP_200_OK)


class SNSGetView(viewsets.ViewSet):

    def list(self, request):
        query = SNS.objects.order_by('order').all()
        serializer = SNSSerializer(query, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, name):
        query = get_object_or_404(SNS, name=name)
        serializer = AboutSerializer(query)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductGetView(viewsets.ViewSet):

    def list(self, request):
        query = Product.objects.order_by('-order').all()
        serializer = ProductSerializer(query, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, product_id):
        query = get_object_or_404(Product, id=id)
        serializer = ProductSerializer(query)

        return Response(serializer.data, status=status.HTTP_200_OK)
