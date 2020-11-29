"""qa_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# import json
from django.contrib import admin
from django.urls import path,include
from django.views.decorators.cache import cache_page
from django.views import View
from django.http import JsonResponse  # ,HttpResponse
# drf接口文档
from rest_framework.documentation import include_docs_urls

def test_api_func(request, *args, **kwargs):
    # for i in request.META:
    #     print(i,request.META.get(i))
    # print("GET:", request.GET.dict())
    # print("POST:", request.POST.dict())
    body = bytes.decode(request.body)
    # body2 = json.loads(body)

    data = {
        'path': request.META.get('PATH_INFO'),
        'method': request.META.get('REQUEST_METHOD'),
        'contentType': request.META.get('CONTENT_TYPE'),
        'queryString': request.META.get('QUERY_STRING'),
        'queryJson': request.GET.dict(),
        'body': body,
    }
    return JsonResponse(data, safe=False, json_dumps_params={'ensure_ascii': False})

class test_api(View):
    def get(self, request, *args, **kwargs):
        return test_api_func(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return test_api_func(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return test_api_func(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return test_api_func(request, *args, **kwargs)


urlpatterns = [
    # django自带后台管理
    path('admin/', admin.site.urls),
    path('testapi/', test_api.as_view()),
    path('qa_backend/',include("apps.qa_backend.urls")),
    #配置docs的url路径
    path('docs/',include_docs_urls(title='api-docs'), name='docs'),
    # path('demo/',include("apps.demo_service.urls")),
]
