from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# 这下面导入的包我看不明白
from django.contrib.auth.decorators import login_required
from django.contrib import auth
# from django.contrib.auth import authenticate,login

# Create your controller here.
def autotest_login(request):
    """登录"""
    if request.POST:
        username = password = ''
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username,password=password)
        if user is not None and user.is_active:
            auth.login(request,user)
            request.session["user"] = username
            response = HttpResponseRedirect('/home/')
            return response
        else:
            return render(request,"login.html",{"error":"login false"})
    return render(request,"login.html")

def autotest_logout(request):
    """退出登录"""
    auth.logout(request)
    return render(request,"login.html")

def home(request):
    """平台首页"""
    projects = ["项目1","项目2"]
    project_details = ["全局配置","API config","测试计划","历史记录","BUG管理","测试报告"]
    return render(request,"index.html",{"projects":projects,"project_details":project_details})

def test(request):
    return HttpResponse("success")