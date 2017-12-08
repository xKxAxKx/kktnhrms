from rest_framework import serializers

from api.models import About, SNS, Product, Inquiry


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = ('name', 'sub_name', 'real_name', 'birthday', 'detail')
