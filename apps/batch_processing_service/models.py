from django.db import models

# Create your models here.
class EventTask(models.Model):
    """事件任务"""
    # 外键—关联测试计划表
    # plan_id = models.BigIntegerField(verbose_name="所属用例id")

    # 处理的事件业务类型
    event_type = models.CharField(verbose_name="业务字段")
    # 事件任务信息(存储Json，不同业务的Json不一致)
    context = models.TextField(verbose_name="事件任务信息")
    # 任务状态（00000）类似二进制处理方式，0未处理，1已处理
    status = models.CharField(verbose_name="任务状态")
    # 是否被消费
    is_finish = models.BooleanField(verbose_name="是否被消费（0未消费1已消费）",default=False)
    # 执行次数
    excute_times = models.IntegerField(verbose_name="任务执行次数",default=0)
    # 执行环境
    env_id = models.IntegerField(verbose_name="执行任务环境")
    # 用例执行者
    executor = models.IntegerField(verbose_name="用例执行者（user_id）")
    # 是否删除
    is_delete = models.BooleanField(verbose_name="是否删除",default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    # def __str__(self):
    #     return self.

    class Meta:
        db_table = "tb_event_task"
        # django的admin界面的后台展示的数据
        verbose_name = "事件任务"
        verbose_name_plural = verbose_name

class EventTaskRecord(models.Model):
    """事件任务"""
    # 外键—关联测试计划表
    # plan_id = models.BigIntegerField(verbose_name="所属用例id")

    # 处理的事件业务类型
    event_type = models.CharField(verbose_name="业务字段")
    # 事件任务信息(存储Json，不同业务的Json不一致)
    context = models.TextField(verbose_name="事件任务信息")
    # 任务状态（00000）类似二进制处理方式，0未处理，1已处理
    status = models.CharField(verbose_name="任务状态")
    # 是否被消费
    is_finish = models.BooleanField(verbose_name="是否被消费（0未消费1已消费）",default=False)
    # 执行次数
    excute_times = models.IntegerField(verbose_name="任务执行次数",default=0)
    # 执行环境
    env_id = models.IntegerField(verbose_name="执行任务环境")
    # 用例执行者
    executor = models.IntegerField(verbose_name="用例执行者（user_id）")
    # 是否删除
    is_delete = models.BooleanField(verbose_name="是否删除",default=False)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    # def __str__(self):
    #     return self.

    class Meta:
        db_table = "tb_event_task"
        # django的admin界面的后台展示的数据
        verbose_name = "事件任务"
        verbose_name_plural = verbose_name


'''
class EventTaskRecord(models.Model):
    """事件任务消费历史表"""
    TASK_STUTAS = (
        (1,1),
        (2,2),
        (3,3),
    )
    # 成功用例数
    pass_total = models.IntegerField(verbose_name="通过数",blank=True,null=True)
    # 失败用例数
    falseTotal = models.IntegerField(verbose_name="失败数",blank=True,null=True)
    # 开始时间时间戳（用例执行时间，结束时计算并返回写入excute_time)
    start_time_stamp = models.BigIntegerField(verbose_name="开始时间戳")
    # 结束时间时间戳
    end_time_stamp = models.BigIntegerField(verbose_name="结束时间戳")
    # 执行时间(s为单位)
    excute_time = models.IntegerField(verbose_name="执行使用时间",blank=True,null=True)
    # 执行用例总数
    excute_total = models.IntegerField(verbose_name="用例执行总数")
    # 任务状态（1、等待2、执行中3、执行完成）
    task_status = models.IntegerField(verbose_name="任务状态（1、等待2、执行中3、执行完成）",choices=TASK_STUTAS)

    class Meta:
        db_table = "tb_event_task_record"
        # django的admin界面的后台展示的数据
        verbose_name = "事件任务记录"
        verbose_name_plural = verbose_name
'''