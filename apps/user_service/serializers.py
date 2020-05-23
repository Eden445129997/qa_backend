from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # fields = ["telephone","username","email","avatar","create_time","update_time","is_active"]

        # 这三种情况不能同时使用
        # 1.取全部字段
        # fields = "__all__"
        # 根据需求排除字段
        # exclude = ["id", "category","author", "publisher"]

        # 2.自定义包含字段
        # fields = ["id", "title", "pub_time"]
        # 输出：[{"id": 1, "title": "python开发", "pub_time": "2011-08-27"},...]
