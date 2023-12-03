from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    OpenApiExample,
    extend_schema
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.goods.serializers import AddGoodSerializer,SeeGoodSerializer
from apps.goods.models import Good

class AddGoodApi(APIView):
    """添加商品api

    Raises:
        ApplicationError: 商品名称或者价格缺失
    Returns:
        请补充完整的商品信息
    """
    # debug的时候用，便于调试
    authentication_classes = []  # Disable authentication
    permission_classes = []  # Disable permission checks
    @extend_schema(
        tags=['添加商品'],
        description="添加商品到用户的购物车",
        methods=['POST'],
        request=AddGoodSerializer,
        responses={
            200: OpenApiTypes.OBJECT,
            400: OpenApiTypes.OBJECT,
        },
        examples=[
            OpenApiExample(
                "添加成功",
                response_only=True,
                summary="添加成功",
                status_codes=["200"],
                description="商品添加成功",
                value={
                    '您选的商品已经添加到您的购物车'
                }
            ),
            OpenApiExample(
                "添加失败",
                summary="添加失败",
                response_only=True,
                status_codes=["400"],
                description="您的商品失败",
                value={
                    "message": "您的商品失败",
                    "extra": {}
                }
            ),
        ]
    )
    def post(self, request: Request) -> Response:
        serializer = AddGoodSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True)==False:
            return Response({"您的请求信息不规范，请与开发者联系"})
        username = serializer.validated_data['username']
        goodname= serializer.validated_data['goodname']
        goodprice=serializer.validated_data['goodprice']
        Good.objects.get_or_create(username=username,Good_name=goodname,Good_price=goodprice)
        return Response({'您选的商品已经添加到您的购物车'})


class SeeGoodApi(APIView):
    """
    查看用户的商品信息api

    Returns:
        返回用户的所有商品信息
    """
                # debug的时候用，便于调试
    authentication_classes = []  # Disable authentication
    permission_classes = []  # Disable permission checks
    @extend_schema(
        tags=['查看商品'],
        description="查看用户的所有商品信息",
        methods=['GET'],
        responses={
            200: SeeGoodSerializer(many=True),
            404: "Not Found",
        },
    )
    def get(self, request):
        # 获取当前请求的用户（假设已经通过认证）
        user = request.username

        # 获取用户的用户名
        username = user.username

        # 查询该用户的所有商品信息
        user_goods = Good.objects.filter(username=username)

        # 序列化商品信息
        serializer = SeeGoodSerializer(user_goods, many=True)

        return Response(serializer.data)