from django.db import models

# Create your models here.

class Project(models.Model):
    """工程表"""
    # 工程id
    # id = models.AutoField()
    # 工程名
    project_name = models.CharField(verbose_name="项目名",max_length=64)
    # 工程描述
    text = models.CharField(verbose_name="描述",max_length=255)
    # 项目负责人
    project_leader = models.CharField("负责人",max_length=64)
    # 状态（启用/不启用）
    status = models.BooleanField(verbose_name="状态（1启用，2不启用）",default=True)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.project_name

    class Meta:
        db_table = "tb_project"
        # django的admin界面的后台展示的数据
        verbose_name = "项目"
        verbose_name_plural = verbose_name

class Host(models.Model):
    """域名表"""
    # 域名id
    # id = models.AutoField()
    # 外键—关联工程表
    project_id = models.BigIntegerField(verbose_name="所属项目id")
    # 环境名
    host_name = models.CharField(verbose_name='域名昵称',max_length=32)
    # host地址
    host = models.CharField(verbose_name='Host域名',max_length=16)
    # 环境描述
    text = models.CharField(verbose_name="描述",max_length=255,blank=True,null=True)
    # 状态：0不启用 1启用
    status = models.BooleanField(verbose_name='状态：0不启用 1启用',default=True)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return "%s:%s"%(self.host_name,self.host)

    class Meta:
        db_table = "tb_host"
        # django的admin界面的后台展示的数据
        verbose_name = "环境"
        verbose_name_plural = verbose_name

class BusiModel(models.Model):
    """业务划分成模块表"""
    # 模块id
    # id = models.AutoField()
    # 外键—关联工程表
    project_id = models.BigIntegerField(verbose_name="所属项目id")
    # 业务名
    busi_name = models.CharField(verbose_name="业务名称",max_length=32)
    # 接口总数
    total = models.IntegerField(verbose_name="接口总数",default=0)
    # 模块描述
    text = models.CharField(verbose_name="描述",max_length=255,blank=True,null=True)
    # 状态（启用/不启用）
    status = models.BooleanField(verbose_name="状态（1启用,0不启用）",default=True)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.busi_name

    class Meta:
        db_table = "tb_busi_model"
        # django的admin界面的后台展示的数据
        verbose_name = "业务"
        verbose_name_plural = verbose_name

class Interface(models.Model):
    """接口表"""
    HTTP_METHOD_CHOICE = (
        ('POST', 'POST'),
        ('GET', 'GET'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE')
    )
    # 接口id
    # id = models.AutoField()
    # 外键—关联模块表
    busi_id = models.BigIntegerField(verbose_name="所属业务id")
    # 接口名称
    api_name = models.CharField(verbose_name="接口名称",max_length=32)
    # 请求方式—1、get2、post
    method = models.IntegerField(verbose_name="请求方式",choices=HTTP_METHOD_CHOICE)
    # 资源路径
    path = models.CharField(verbose_name="资源路径",max_length=128)
    # 默认入参——存储数据的时候存储数组，每个key存储字典，键为key，值为数据类型
    defaultData = models.TextField(verbose_name="默认入参",default="{}")
    # 接口描述
    text = models.CharField(verbose_name="描述",max_length=255,blank=True,null=True)
    # 状态（0 不启用，1 启用）
    status = models.BooleanField(verbose_name="状态",default=True)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return "%s:%s"%(self.api_name,self.path)

    class Meta:
        db_table = "tb_interfact"
        # django的admin界面的后台展示的数据
        verbose_name = "接口"
        verbose_name_plural = verbose_name

class TestPlan(models.Model):
    """测试计划表"""
    # 计划id
    # id = models.AutoField()
    # 外键—关联工程表
    project_id = models.BigIntegerField(verbose_name="所属项目id")
    # 计划名称
    plan_name = models.CharField(verbose_name="测试计划",max_length=32)
    # 计划创建人
    creater = models.CharField(verbose_name="计划创建者",max_length=8)
    # 计划描述
    text = models.CharField(verbose_name="描述",max_length=255,blank=True,null=True)
    # 状态（启用/不启用）如果不启用，页面上则看不到
    status = models.BooleanField(verbose_name="状态（1启用，2不启用）—如果不启用，页面上则看不到",default=True)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return "%s — %s"%(self.plan_name,self.creater)

    class Meta:
        db_table = "tb_test_plan"
        # django的admin界面的后台展示的数据
        verbose_name = "测试计划"
        verbose_name_plural = verbose_name

class TestCase(models.Model):
    """测试用例表"""
    # 用例id
    # id = models.AutoField()
    # 外键—关联工程表
    plan_id = models.BigIntegerField(verbose_name="所属计划id")
    # 用例名称
    case_name = models.CharField(verbose_name="用例名称",max_length=32)
    # 用例描述
    text = models.CharField(verbose_name="描述",max_length=255,blank=True,null=True)
    # 状态（启用/不启用）如果不启用，则执行测试计划的时候，该用例不会被执行
    status = models.BooleanField(verbose_name="状态（启用/不启用）如果不启用，则执行测试计划的时候，该用例不会被执行",default=True)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return self.case_name

    class Meta:
        db_table = "tb_test_case"
        # django的admin界面的后台展示的数据
        verbose_name = "测试用例"
        verbose_name_plural = verbose_name

class TestCaseDetail(models.Model):
    """测试细节表(测试参数表)"""
    """
    比如用例ABCDE，如果c启用mock，则写入mock返回值，c校验直接为True，并直接取mock里面的值
    """

    # 用例id
    # id = models.AutoField()
    # 外键—关联用例表
    case_id = models.BigIntegerField(verbose_name="所属用例id")
    # 请求的url
    uri_id = models.BigIntegerField(verbose_name="请求资源地址")
    # 请求头
    input_header = models.TextField(verbose_name="请求头",default="{}")
    # 入参
    input_parameter = models.TextField(verbose_name="请求入参",default="{}")
    # mock状态（0 不启用mock，1启用mock）
    mock_status = models.BooleanField(verbose_name="mock状态（0 不启用mock，1启用mock）",default=False)
    # mock返回
    mock_response = models.TextField(verbose_name="mock的返回值",default="{}")
    # 用例描述
    text = models.CharField(verbose_name="用例描述",max_length=255,blank=True,null=True)
    # 校验点
    checkpoint = models.TextField(verbose_name="校验点",default="{}")
    # 排序顺序
    case_sort = models.IntegerField(verbose_name="用例排序顺序",default=0)
    # 状态（0 不启用，1启用）
    status = models.BooleanField(verbose_name="状态",default=True)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return "case_id：%s，参数：%s"%(self.case_id,self.input_parameter)

    class Meta:
        db_table = "tb_test_case_detail"
        # django的admin界面的后台展示的数据
        verbose_name = "用例参数"
        verbose_name_plural = verbose_name

class ApiTestReport(models.Model):
    """接口测试任务报告"""
    TASK_STUTAS = (
        (1,1),
        (2,2),
        (3,3),
    )
    # 执行者
    executor = models.CharField(verbose_name="计划执行者",max_length=32)
    # 环境
    env = models.CharField(verbose_name="执行任务环境",max_length=32)
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
    task_status = models.IntegerField(verbose_name="任务状态（1、等待执行2、执行中3、执行完成）",choices=TASK_STUTAS)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_api_test_report"
        # django的admin界面的后台展示的数据
        verbose_name = "接口测试报告"
        verbose_name_plural = verbose_name

class ApiTestReportDetail(models.Model):
    """接口测试报告细节"""
    # 外键关联用例id
    case_id = models.BigIntegerField(verbose_name="所属用例id")
    # 外键关联报告id
    report_id = models.BigIntegerField(verbose_name="所属报告id")
    # 请求头
    input_header = models.TextField(verbose_name="请求头",default="{}")
    # 入参
    input_parameter = models.TextField(verbose_name="请求入参",default="{}")
    # 响应参数
    output_parameter = models.TextField(verbose_name="响应参数",blank=True,null=True)
    # 报错记录
    error_record = models.TextField(verbose_name="报错记录",blank=True,null=True)
    # 是否mock，该历史记录是否使用mock
    is_mock = models.BooleanField(verbose_name="是否mock",default=False)
    # 排序顺序
    case_sort = models.IntegerField(verbose_name="用例排序顺序",default=0)
    # 用例执行开始时间
    start_time_stamp = models.BigIntegerField(verbose_name="开始时间戳")
    # 用例结束时间时间戳
    end_time_stamp = models.BigIntegerField(verbose_name="结束时间戳")
    # 执行时间(s为单位)
    excute_time = models.IntegerField(verbose_name="执行使用时间",blank=True,null=True)
    # 创建时间
    create_time = models.DateTimeField(verbose_name='创建时间',auto_now_add=True)
    # 最后变动时间
    update_time = models.DateTimeField(verbose_name='更新时间',auto_now=True)

    objects = models.Manager()

    class Meta:
        db_table = "tb_api_test_report_detail"
        # django的admin界面的后台展示的数据
        verbose_name = "接口测试报告细节"
        verbose_name_plural = verbose_name