# Generated by Django 3.0.6 on 2020-07-24 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApiTestReport',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('executor', models.CharField(max_length=32, null=True, verbose_name='计划执行者')),
                ('host', models.CharField(max_length=32, null=True, verbose_name='执行任务环境')),
                ('pass_total', models.IntegerField(blank=True, null=True, verbose_name='通过数')),
                ('false_total', models.IntegerField(blank=True, null=True, verbose_name='失败数')),
                ('time_taken', models.CharField(blank=True, max_length=32, null=True, verbose_name='执行使用时间')),
                ('total', models.IntegerField(verbose_name='用例执行总数')),
                ('task_status', models.CharField(choices=[('等待执行', '等待执行'), ('执行中', '执行中'), ('完成', '完成'), ('失败', '失败')], max_length=16, verbose_name='任务状态（1、等待执行2、执行中3、成功4、失败）')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '接口测试报告',
                'verbose_name_plural': '接口测试报告',
                'db_table': 'tb_api_test_report',
            },
        ),
        migrations.CreateModel(
            name='ApiTestReportDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('case_id', models.IntegerField(verbose_name='所属用例id')),
                ('report_id', models.IntegerField(verbose_name='所属报告id')),
                ('api_name', models.CharField(max_length=32, null=True, verbose_name='接口名称')),
                ('url', models.CharField(max_length=128, null=True, verbose_name='请求地址')),
                ('header', models.TextField(default='{}', verbose_name='请求头')),
                ('data', models.TextField(default='{}', verbose_name='请求入参')),
                ('response', models.TextField(blank=True, null=True, verbose_name='响应参数')),
                ('error_record', models.TextField(blank=True, null=True, verbose_name='报错记录')),
                ('fail_times', models.IntegerField(null=True, verbose_name='用例排序顺序')),
                ('is_mock', models.BooleanField(default=False, verbose_name='是否mock')),
                ('sort', models.IntegerField(default=0, verbose_name='用例排序顺序')),
                ('start_time', models.CharField(max_length=32, null=True, verbose_name='开始时间')),
                ('stop_time', models.CharField(max_length=32, null=True, verbose_name='结束时间')),
                ('time_taken', models.CharField(blank=True, max_length=32, null=True, verbose_name='执行使用时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '接口测试报告细节',
                'verbose_name_plural': '接口测试报告细节',
                'db_table': 'tb_api_test_report_detail',
            },
        ),
        migrations.CreateModel(
            name='BusiModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_id', models.IntegerField(verbose_name='所属项目id')),
                ('busi_name', models.CharField(max_length=32, verbose_name='业务名称')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='描述')),
                ('status', models.BooleanField(default=True, verbose_name='状态（1启用,0不启用）')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '业务',
                'verbose_name_plural': '业务',
                'db_table': 'tb_busi_model',
            },
        ),
        migrations.CreateModel(
            name='CheckPoint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('case_detail_id', models.IntegerField(verbose_name='所属的case_detail')),
                ('check_object', models.CharField(max_length=64, verbose_name='检查对象，jsonpath表达式')),
                ('check_method', models.CharField(choices=[('assertEqual', 'assertEqual'), ('assertNotEqual', 'assertNotEqual'), ('assertIn', 'assertIn'), ('assertNotIn', 'assertNotIn')], max_length=16, verbose_name='校验方法')),
                ('check_value', models.TextField(verbose_name='校验的比对值')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='用例描述')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '检查点',
                'verbose_name_plural': '检查点',
                'db_table': 'tb_check_point',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_id', models.IntegerField(verbose_name='所属项目id')),
                ('host_name', models.CharField(max_length=32, verbose_name='域名昵称')),
                ('host', models.CharField(max_length=16, verbose_name='Host域名')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='描述')),
                ('status', models.BooleanField(default=True, verbose_name='状态：0不启用 1启用')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '环境',
                'verbose_name_plural': '环境',
                'db_table': 'tb_host',
            },
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_id', models.IntegerField(default=0, null=True, verbose_name='所属项目id')),
                ('busi_id', models.IntegerField(null=True, verbose_name='所属业务id')),
                ('api_name', models.CharField(max_length=32, verbose_name='接口名称')),
                ('method', models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT'), ('DELETE', 'DELETE')], max_length=255, verbose_name='请求方式')),
                ('path', models.CharField(max_length=128, verbose_name='资源路径')),
                ('default_data', models.TextField(default='{}', verbose_name='默认入参')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='描述')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '接口',
                'verbose_name_plural': '接口',
                'db_table': 'tb_interface',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=64, verbose_name='项目名')),
                ('text', models.CharField(max_length=255, verbose_name='描述')),
                ('project_leader', models.CharField(max_length=64, verbose_name='负责人')),
                ('status', models.BooleanField(default=True, verbose_name='状态（1启用，2不启用）')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '项目',
                'verbose_name_plural': '项目',
                'db_table': 'tb_project',
            },
        ),
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('plan_id', models.IntegerField(verbose_name='所属计划id')),
                ('case_name', models.CharField(max_length=32, verbose_name='用例名称')),
                ('sort', models.IntegerField(default=0, verbose_name='排序')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='描述')),
                ('status', models.BooleanField(default=True, verbose_name='状态（启用/不启用）如果不启用，则执行测试计划的时候，该用例不会被执行')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '测试用例',
                'verbose_name_plural': '测试用例',
                'db_table': 'tb_test_case',
            },
        ),
        migrations.CreateModel(
            name='TestCaseDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('case_id', models.IntegerField(verbose_name='所属用例id')),
                ('interface_id', models.IntegerField(verbose_name='请求资源地址')),
                ('reconnection_times', models.IntegerField(default=3, verbose_name='重连次数')),
                ('wait_time', models.IntegerField(default=10, verbose_name='最长等待时长')),
                ('headers', models.TextField(default='{}', verbose_name='请求头')),
                ('data', models.TextField(default='{}', verbose_name='请求入参')),
                ('mock_status', models.BooleanField(default=False, verbose_name='mock状态（0 不启用mock，1启用mock）')),
                ('mock_response', models.TextField(default='{}', verbose_name='mock的返回值')),
                ('expression_status', models.BooleanField(default=False, verbose_name='表达式状态（0 不启用jsonpath捕捉参数化，1 启用jsonpath捕捉参数化）')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='用例描述')),
                ('sort', models.IntegerField(default=0, verbose_name='用例排序顺序')),
                ('status', models.BooleanField(default=True, verbose_name='状态')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '用例参数',
                'verbose_name_plural': '用例参数',
                'db_table': 'tb_test_case_detail',
            },
        ),
        migrations.CreateModel(
            name='TestPlan',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('project_id', models.IntegerField(verbose_name='所属项目id')),
                ('plan_name', models.CharField(max_length=32, verbose_name='测试计划')),
                ('creater', models.CharField(max_length=8, verbose_name='计划创建者')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='描述')),
                ('status', models.BooleanField(default=True, verbose_name='状态（1启用，2不启用）—如果不启用，页面上则看不到')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '测试计划',
                'verbose_name_plural': '测试计划',
                'db_table': 'tb_test_plan',
            },
        ),
    ]
