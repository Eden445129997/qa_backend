# from django.shortcuts import render

from rest_framework import views
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import UserSerializer

# django自带的上一次登录时间
from django.utils.timezone import now

User = get_user_model()

class LoginView(views.APIView):
    """登录接口"""
    def post(self,request):
        serializer = AuthTokenSerializer(data=request.data,context={"request":request})
        # print("="*500)
        if serializer.is_valid():
            user = serializer.validated_data.get("user")
            # 更新最后登录时间
            user.last_login = now()
            # 保存模型的更新操作
            user.save()
            user_serializer = UserSerializer(user)
            return Response(data={"user":user_serializer.data})
        else:
            print(serializer.errors)
            return Response(data={"message":"数据提交错误"})