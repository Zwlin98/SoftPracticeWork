# Generated by Django 2.1.3 on 2018-11-13 15:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerName', models.CharField(max_length=30, verbose_name='旅客姓名')),
                ('customerGender', models.CharField(choices=[('男', '男'), ('女', '女')], max_length=5, verbose_name='性别')),
                ('customerId', models.CharField(max_length=18, primary_key=True, serialize=False, verbose_name='旅客身份证号码')),
                ('customerPhoneNumber', models.CharField(max_length=11, verbose_name='手机号码')),
                ('roomId', models.CharField(max_length=10, verbose_name='房间号')),
                ('roomType', models.CharField(choices=[('大床房', '大床房'), ('标间', '标间'), ('钟点房', '钟点房')], max_length=8, verbose_name='房间类型')),
                ('customerCheckInTime', models.DateTimeField(default=datetime.datetime.now, verbose_name='入住时间')),
                ('customerStayTime', models.IntegerField(verbose_name='入住时长')),
            ],
        ),
    ]
