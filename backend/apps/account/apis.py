import os
import requests

from apps.api.exceptions import ApplicationError
from django.contrib.auth import get_user_model
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import (
    OpenApiExample,
    OpenApiParameter,
    OpenApiResponse,
    extend_schema
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserLoginSerializer, UserSerializer


class UserRegisterApi(APIView):
    """用户注册接口

    Returns:
        Response: 用户登录成功

    Raises:
        ApplicationError: 信息不合法
        ApplicationError: 必填信息欠缺
        ApplicationError: 与已有用户用户名重复
    """
    permission_classes = []

    @extend_schema(
        tags=['用户'],
        description="用户注册",
        methods=['POST'],
        request=UserSerializer,
        responses={
            200: OpenApiTypes.OBJECT,
            400: OpenApiTypes.OBJECT,
        },
        examples=[
            OpenApiExample(
                "注册成功",
                response_only=True,
                summary="注册成功",
                status_codes=["200"],
                description="用户注册成功",
                value={
                    "message": "用户注册成功"
                }
            ),
            OpenApiExample(
                "必填信息欠缺",
                summary="必填信息欠缺",
                response_only=True,
                status_codes=["400"],
                description="必填信息欠缺",
                value={
                    "message": "Validation error",
                    "extra": {
                        "fields": {
                            "username": [
                                "该字段是必填项。"
                            ]
                        }
                    }
                }
            ),
            OpenApiExample(
                "与已有用户用户名重复",
                summary="与已有用户用户名重复",
                response_only=True,
                status_codes=["400"],
                description="与已有用户用户名重复",
                value={
                    "message": "Validation error",
                    "extra": {
                        "fields": {
                            "username": [
                                "已存在一位使用该名字的用户。"
                            ]
                        }
                    }
                }
            ),
            OpenApiExample(
                "信息不合法",
                summary="信息不合法",
                response_only=True,
                status_codes=["400"],
                description="信息不合法",
                value={
                    "message": "Validation error",
                    "extra": {
                        "fields": {
                            "gender": [
                                "“m5ale” 不是合法选项。"
                            ],
                            "user_type": [
                                "“ind2ividual” 不是合法选项。"
                            ]
                        }
                    }
                }
            ),
        ]
    )
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "用户注册成功"})


class UserLoginApi(APIView):
    """用户登录接口，使用用户名+密码登录

    Raises:
        ApplicationError: 用户名对应用户不存在
        ApplicationError: 密码错误

    Returns:
        Response: 用户名以及token信息
    """
    permission_classes = []

    @extend_schema(
        tags=['用户'],
        description="用户登录(用户名+密码)",
        methods=['POST'],
        request=UserLoginSerializer,
        responses={
            200: OpenApiTypes.OBJECT,
            400: OpenApiTypes.OBJECT,
        },
        examples=[
            OpenApiExample(
                "登录成功",
                response_only=True,
                summary="登录成功",
                status_codes=["200"],
                description="用户登录成功",
                value={
                    "username": "test",
                    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9",
                    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9",
                    "expire": 604800
                }
            ),
            OpenApiExample(
                "密码错误",
                summary="密码错误",
                response_only=True,
                status_codes=["400"],
                description="密码错误",
                value={
                    "message": "密码错误",
                    "extra": {}
                }
            ),
            OpenApiExample(
                "用户不存在",
                summary="用户不存在",
                response_only=True,
                status_codes=["400"],
                description="用户名对应用户不存在",
                value={
                    "message": "用户名对应用户不存在",
                    "extra": {}
                }
            ),
        ]
    )
    def post(self, request: Request) -> Response:
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = get_user_model().objects.get(username=serializer.validated_data["username"])
        except get_user_model().DoesNotExist:
            raise ApplicationError("用户名对应用户不存在")
        if user.check_password(serializer.validated_data["password"]):
            refresh: RefreshToken = RefreshToken.for_user(user)  # 生成refresh token
            return Response({
                "username": user.username,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "expire": refresh.access_token.payload["exp"] - refresh.access_token.payload["iat"],
            })
        else:
            raise ApplicationError("密码错误")


class WXLoginApi(APIView):
    """微信登录API

    Raises:
        ApplicationError: 微信登录功能未启用
        ApplicationError: 未获取到openid
        ApplicationError: Wechat code not provided
        ApplicationError: Corresponding user not found
        ApplicationError: Wechat user openid is empty

    Returns:
        Response: 登录响应
    """
    permission_classes = []

    def get_wx_userid(self, code: str) -> str:
        appid = os.environ.get("WX_APPID", None)
        appsecret = os.environ.get("WX_APPSECRET", None)
        if appid is None or appsecret is None:
            raise ApplicationError("微信登录功能未启用")
        base_url = 'https://api.weixin.qq.com/sns/jscode2session'
        url = "{}?appid={}&secret={}&js_code={}&grant_type=authorization_code".format(
            base_url, appid, appsecret, code
        )
        response = requests.get(url)
        try:
            wx_openid: str = response.json()['openid']
        except KeyError:  # 未获取到openid
            raise ApplicationError(
                message=response.json().get('errmsg'),
                extra={
                    "errcode": response.json().get('errcode'),
                    "reference": "https://developers.weixin.qq.com/doc/oplatform/Return_codes/Return_code_descriptions_new.html"
                }
            )
        else:
            return wx_openid

    def post(self, request: Request) -> Response:
        code = request.data.get("code", None)
        if code is None:
            raise ApplicationError(
                message="Wechat code not provided",
                extra={
                    "reference": "https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Wechat_webpage_authorization.html#0"
                }
            )
        wx_openid = self.get_wx_userid(code)
        if wx_openid:  # openid不为空
            try:
                user = get_user_model().objects.get(wx_openid=wx_openid)
            except get_user_model().DoesNotExist:
                raise ApplicationError("Corresponding user not found")
            else:
                refresh: RefreshToken = RefreshToken.for_user(user)
                return Response({
                    "username": user.username,
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "expire": refresh.access_token.payload["exp"] - refresh.access_token.payload["iat"],
                })
        else:  # openid为空
            raise ApplicationError("Wechat user openid is empty")


class WXBindApi(APIView):
    """绑定当前登陆账户与微信用户
    """
    permission_classes = [IsAuthenticated]

    def post(self, request: Request) -> Response:
        pass


class WXTrialApi(APIView):
    """微信小程序试用接口

    利用微信openid查询, 如果用户不存在则创建
    """
    permission_classes = []

    def get_wx_userid(self, code: str) -> str:
        appid = os.environ.get("WX_APPID", None)
        appsecret = os.environ.get("WX_APPSECRET", None)
        if appid is None or appsecret is None:
            raise ApplicationError("微信登录功能未启用")
        base_url = 'https://api.weixin.qq.com/sns/jscode2session'
        url = "{}?appid={}&secret={}&js_code={}&grant_type=authorization_code".format(
            base_url, appid, appsecret, code
        )
        response = requests.get(url)
        try:
            wx_openid: str = response.json()['openid']
        except KeyError:  # 未获取到openid
            raise ApplicationError(
                message=response.json().get('errmsg'),
                extra={
                    "errcode": response.json().get('errcode'),
                    "reference": "https://developers.weixin.qq.com/doc/oplatform/Return_codes/Return_code_descriptions_new.html"
                }
            )
        else:
            return wx_openid

    def post(self, request: Request) -> Response:
        code = request.data.get("code", None)
        if code is None:
            raise ApplicationError(
                message="Wechat code not provided",
                extra={
                    "reference": "https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/Wechat_webpage_authorization.html#0"
                }
            )
        wx_openid = self.get_wx_userid(code)
        if wx_openid:  # openid不为空
            user = get_user_model().objects.get_or_create(wx_openid=wx_openid)
            refresh: RefreshToken = RefreshToken.for_user(user)
            return Response({
                "username": user.username,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "expire": refresh.access_token.payload["exp"] - refresh.access_token.payload["iat"],
            })
        else:  # openid为空
            raise ApplicationError("Wechat user openid is empty")
