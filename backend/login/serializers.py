from rest_framework.serializers import ModelSerializer
from .models import UserInfo



class UserInfoListSerializer(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class UserInfoSerializer(ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
    extra_kwargs = {
        'password': {'required': False},
        'account': {'required': False},
        'update_time': {'required': False},
        'date_time': {'required': False}
    }


