from rest_framework import serializers
from apps.demo_service import models

# rest_framework的序列化
class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DemoModel
        fields = "__all__"

        # 这三种情况不能同时使用
        # 1.取全部字段
        # fields = "__all__"
        # 根据需求排除字段
        # exclude = ["id", "category","author", "publisher"]

        # 2.自定义包含字段
        # fields = ["id", "title", "pub_time"]
        # 输出：[{"id": 1, "title": "python开发", "pub_time": "2011-08-27"},...]


# serializers.Serializer需要指定序列化的参数
# 1、序列化数据
# 2、验证表单数据
# 3、可以创建数据、修改数据
class Serializers(serializers.Serializer):
    # read_only=True的意思是，当使用改序列化器做表单验证的时候不能够写id这个字段，但是读取的时候会返回id
    id = serializers.IntegerField(read_only=True)
    # required=True意思是必填
    text = serializers.CharField(required=True)
