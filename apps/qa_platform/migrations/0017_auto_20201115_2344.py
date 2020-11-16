# Generated by Django 3.0.6 on 2020-11-15 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_platform', '0016_auto_20201113_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='content_type',
            field=models.CharField(choices=['text/html', 'text/plain', 'text/xml', 'application/x-www-form-urlencoded', 'application/json', 'application/xml', 'application/msword', 'application/pdf', 'image/gif', 'image/jpeg', 'image/png'], max_length=128, verbose_name='http报文body序列化类型content_type'),
        ),
    ]