from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Good

class AddGoodSerializer(serializers.Serializer):
    goodname = serializers.CharField(
        max_length=150,
        required=True
    )
    goodprice= serializers.IntegerField(
        required=True
    )
    username=serializers.CharField(
        max_length=128,
        required=True
    )

class SeeGoodSerializer(serializers.Serializer):
    class Meta:
        model = Good
        fields = ['goodname', 'goodprice', 'username']