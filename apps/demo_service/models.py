from django.db import models

class DemoModel(models.Model):
    """demo模型"""

    text = models.CharField(max_length=16)

    class Meta:
        db_table = "tb_demo"
        # django的admin界面的后台展示的数据
        verbose_name = "测试数据"
        verbose_name_plural = verbose_name

    # 为了让view视图能够使用model.object.all()获取表对象所有的数据
    objects = models.Manager()

    # def __str__(self):
    #     return self.text