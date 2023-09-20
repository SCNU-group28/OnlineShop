from django.urls import path
from .apis import UserRegisterApi, UserLoginApi


urlpatterns = [
    path("register/", UserRegisterApi.as_view(), name="register"),
    path("login/", UserLoginApi.as_view(), name="login"),
]
