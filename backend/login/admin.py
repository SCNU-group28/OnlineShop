from django.contrib import admin

#从当前模型那里导入模型
from .models import UserInfo

admin.site.register(UserInfo)
# Register your models here.
