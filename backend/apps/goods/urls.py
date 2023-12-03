from django.urls import path
from .apis import AddGoodApi,SeeGoodApi

urlpatterns = [
    path("addgood/", AddGoodApi.as_view(), name="addgood"),
    path("seegood/",SeeGoodApi.as_view(),name="seegood"),
]
