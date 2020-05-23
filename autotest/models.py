from django.db import models

# Create your models here.
class Project(models.Model):
    """工程表"""
    # 工程id
    id = models.AutoField()
    # 工程名
    project_name = models.CharField(max_length=64)
    # 工程描述
    text = models.CharField(max_length=255)
    # 项目负责人
    project_leader = models.CharField(max_length=64)
    # 状态（启用/不启用）
    status = models.BooleanField(default=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)
    # 最后变动时间
    update_time = models.DateTimeField()

    def __str__(self):
        return self.project_name

class Environment(models.Model):
    """项目环境表"""
    # 环境id
    id = models.AutoField()
    # 外键—关联工程表
    project_id = models.ForeignKey("Project",on_delete=models.CASCADE)
    # 环境名
    environment_name = models.CharField(max_length=32)
    # 目标地址
    host = models.CharField(max_length=16)
    # 端口
    port = models.CharField(max_length=8)
    # 环境描述
    text = models.CharField(max_length=255)
    # 状态（启用/不启用）
    status = models.BooleanField(default=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)
    # 最后变动时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.environment_name

class ProjectModel(models.Model):
    """模块表"""
    # 模块id
    id = models.AutoField()
    # 外键—关联工程表
    project_id = models.ForeignKey("Project",on_delete=models.CASCADE)
    # 模块名
    type_name = models.CharField(max_length=32)
    # 接口总数
    total = models.CharField(max_length=16)
    # 模块描述
    text = models.CharField(max_length=255)
    # 状态（启用/不启用）如果不启用，页面上则看不到
    status = models.BooleanField(default=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)
    # 最后变动时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type_name

class Interface(models.Model):
    """接口表"""
    # 接口id
    id = models.AutoField()
    # 外键—关联模块表
    type_id = models.ForeignKey("InterfaceType",on_delete=models.CASCADE)
    # 接口名称
    api_name = models.CharField(max_length=32)
    # 请求方式
    request_method = models.CharField(max_length=8)
    # 路由
    path = models.CharField(max_length=128)
    # 默认入参——存储数据的时候存储数组，每个key存储字典，键为key，值为数据类型
    defaultData = models.TextField()
    # 接口描述
    text = models.CharField(max_length=255)
    # 状态（0 不启用，1 启用，2 开发，3 测试）
    status = models.CharField(default="1")
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)
    # 最后变动时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.api_name

class TestPlan(models.Model):
    """测试计划表"""
    # 计划id
    id = models.AutoField()
    # 外键—关联工程表
    project_id = models.ForeignKey("Project",on_delete=models.CASCADE)
    # 计划名称
    plan_name = models.CharField(max_length=32)
    # 计划创建人
    creater = models.CharField(max_length=8)
    # 计划描述
    text = models.CharField(max_length=255)
    # 状态（启用/不启用）如果不启用，页面上则看不到
    status = models.BooleanField(default=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)
    # 最后变动时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plan_name

class TestCase(models.Model):
    """测试用例表"""
    # 用例id
    id = models.AutoField()
    # 外键—关联工程表
    plan_id = models.ForeignKey("TestPlan",on_delete=models.CASCADE)
    # 用例名称
    case_name = models.CharField(max_length=32)
    # 用例描述
    text = models.CharField(max_length=255)
    # 状态（启用/不启用）如果不启用，则执行测试计划的时候，该用例不会被执行
    status = models.BooleanField(default=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)
    # 最后变动时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.case_name

class CaseDetails(models.Model):
    """测试细节表"""
    # 用例id
    id = models.AutoField()
    # 外键—关联用例表
    case_id = models.ForeignKey("TestCase",on_delete=models.CASCADE)
    # 入参
    request = models.TextField()
    # mock返回
    mockResponse = models.CharField(max_length=32)
    # 用例描述
    text = models.CharField(max_length=255)
    # 状态（0 不启用，1启用，2 启用mock）
    status = models.BooleanField(default=True)
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)
    # 最后变动时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.case_id

class History(models.Model):
    """执行历史表"""
    # 历史id
    # id = models.AutoField()
    # 外键—关联测试计划表
    plan_id = models.ForeignKey("TestPlan",on_delete=models.CASCADE)
    # 成功用例数
    pass_total = models.IntegerField()
    # 失败用例数
    falseTotal = models.IntegerField()
    # 用例执行所需时间
    excuteTime = models.CharField(max_length=16)
    # 执行用例总数
    excuteTotal = models.CharField(max_length=16)
    # 用例描述
    text = models.CharField(max_length=255)
    # 状态（0 不启用，1启用，2 启用mock）
    status = models.BooleanField(default=True)
    # 创建时间
    startTime = models.DateTimeField()
    # 创建时间
    end_time = models.DateTimeField()
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)
    # 最后变动时间
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return TestCase.case_name

class HistoryDeatails(models.Model):
    """执行历史表"""
    # 历史id
    id = models.AutoField()
    # 外键—关联测试计划表
    history_id = models.ForeignKey("History",on_delete=models.CASCADE)
    # 成功用例数
    case_details = models.IntegerField()
    # 失败用例数
    request = models.IntegerField()
    # 用例执行所需时间
    response = models.TextField()
    # 执行用例总数
    errorRecord = models.TextField()
    # 创建时间
    create_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return TestCase.case_name







