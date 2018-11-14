from django.db import models

# Create your models here.

from datetime import datetime


class Customer(models.Model):
    gender_choice = (
        ("男", "男"),
        ("女", "女")
    )

    customerName = models.CharField(max_length=30, verbose_name="旅客姓名")

    customerGender = models.CharField(max_length=5, verbose_name="性别", choices=gender_choice)

    customerId = models.CharField(max_length=18, primary_key=True, verbose_name="旅客身份证号码")

    customerPhoneNumber = models.CharField(max_length=11,verbose_name="手机号码")

    roomId = models.CharField(max_length=10, verbose_name="房间号")

    roomtype = (
        ("大床房", "大床房"),
        ("标间", "标间"),
        ("钟点房", "钟点房")
    )

    roomType = models.CharField(max_length=8, verbose_name="房间类型", choices=roomtype)

    customerCheckInTime = models.DateTimeField(default=datetime.now, verbose_name="入住时间")

    customerStayTime = models.IntegerField(verbose_name="入住时长")
