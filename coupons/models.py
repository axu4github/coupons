# -*- coding:utf-8 -*-

"""
数据库表管理
"""

from __future__ import unicode_literals
from django.db import models


class Coupons(models.Model):
    """
    优惠券表

    存储所有关于优惠券的信息
    """

    name = models.CharField(
        unique=True, blank=False, max_length=50, help_text="优惠券名称")
    describe = models.CharField(
        blank=False, default="", max_length=200, help_text="优惠券描述")
    url = models.URLField(
        blank=False, help_text="优惠券网址")
    website = models.CharField(
        blank=False, default="", max_length=50, help_text="优惠券网站")
    classification = models.CharField(
        blank=False, default="", max_length=20, help_text="优惠券分类")
    created = models.DateTimeField(
        blank=False, auto_now_add=True, help_text="优惠券创建时间")
    modified = models.DateTimeField(
        blank=False, auto_now=True, help_text="优惠券修改时间")
    enabled = models.BooleanField(
        blank=False, default="True", help_text="优惠券已经启用")
