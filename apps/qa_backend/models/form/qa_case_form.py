from django import forms

class AutoAddCaseApiform(forms.Form):
    # 2、模板中的元素
    name = forms.CharField(min_length=6,error_messages={"requird":"用户名不能为空","min_length":"最小长度为6"})