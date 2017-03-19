# -*- coding:utf-8 -*-

"""
单元测试

"""

from django.test import TestCase
from django.conf import settings
from coupons.models import Coupons


class EnvTest(TestCase):

    def test_load_custom_settings(self):
        """
        加载自定义配置测试

        测试修改了配置文件目录（由默认创建的'${BASE_DIR}/coupons'修改为${BASE_DIR}/'configs'）是否可以顺利加载配置
        """

        import os
        self.assertIsNotNone(settings.SECRET_KEY)
        self.assertEqual(settings.BASE_DIR, os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))))


class DBTest(TestCase):
    """
    数据库测试
    """

    def test_coupons_create_one_row(self):
        # 从数据库中取出的中文数据是`Unicode`编码的，所以为了后面的验证，这里也要使用`Unicode`编码声明。
        name = u"测试_添加优惠券表_一行_名称"
        describe = u"测试_添加优惠券表_一行_描述"
        url = "http://www.test.com/add_one_row_by_url"
        classification = u"测试_添加优惠券表_一行_分类"

        Coupons.objects.create(
            name=name,
            describe=describe,
            url=url,
            classification=classification)

        coupon = Coupons.objects.get(name=name)

        self.assertEqual(coupon.describe, describe)
        self.assertEqual(coupon.url, url)
        self.assertEqual(coupon.classification, classification)
        self.assertTrue(coupon.enabled)
