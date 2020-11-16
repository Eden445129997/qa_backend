# Generated by Django 3.0.6 on 2020-11-12 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa_platform', '0008_auto_20201112_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiassert',
            name='data_id',
            field=models.ForeignKey(blank=True, db_column='data_id', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='qa_platform.ApiCaseData', verbose_name='所属数据id'),
        ),
        migrations.AlterField(
            model_name='apiassert',
            name='model_id',
            field=models.ForeignKey(blank=True, db_column='model_id', db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='qa_platform.ApiCaseModel', verbose_name='关联模型id'),
        ),
    ]