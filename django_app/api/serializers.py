from rest_framework import serializers

from api.models import About, SNS, Product, Inquiry


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ('name', 'sub_name', 'real_name', 'birthday', 'detail')


class SNSSerializer(serializers.ModelSerializer):

    class Meta:
        model = SNS
        fields = ('name', 'account_name', 'url')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'url', 'detail')


class InquirySerializer(serializers.ModelSerializer):

    class Meta:
        model = Inquiry
        fields = '__all__'

    def create(self, validated_data):
        return Inquiry.objects.create(**validated_data)
