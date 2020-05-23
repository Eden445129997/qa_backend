from django.core import serializers
from datetime import date

# serializers源码
# BUILTIN_SERIALIZERS = {
#     "xml": "django.core.serializers.xml_serializer",
#     "python": "django.core.serializers.python",
#     "json": "django.core.serializers.json",
#     "yaml": "django.core.serializers.pyyaml",
# }

def query_set_serializers(query_set_class):
    """ 目的：方便前端开发，接口风格统一如viewset
        自定义统一rest_framework接口风格创建的func
        入参传入query_set的类
        原数据："[{\"model\": \"test_platform.project\", \"pk\": 1, \"fields\": {\"project_name\": \"\\u6572\\u9177\", \"text\": \"\\u9879\\u76eetext\", \"project_leader\": \"Eden\", \"status\": true, \"create_time\": \"2020-04-30T17:36:06Z\", \"update_time\": \"2020-04-30T17:36:09Z\"}}, {\"model\": \"test_platform.project\", \"pk\": 3, \"fields\": {\"project_name\": \"\\u6572\\u725b\", \"text\": \"\\u9879\\u76eetext\", \"project_leader\": \"Eden\", \"status\": true, \"create_time\": \"2020-05-09T11:12:03Z\", \"update_time\": \"2020-05-09T11:12:06Z\"}}]"
        转换后数据：
    """
    second_list = []
    first_list = serializers.serialize("python", query_set_class)
    for list_data in first_list:
        list_data = list_data.get("fields")
        # 时间单独格式化处理
        if 'create_time' in list_data.keys():
            list_data['create_time'] = list_data['create_time'].strftime('%Y-%m-%d')
        second_list.append(list_data)
    # print(type(second_list))
    return second_list

def custom_serializers(model,data_list):
    field = [f for f in model.Project._meta.fields]
    # print(type(field))
    # print (field)
    for msg in field:
        print(msg.name,msg.verbose_name)