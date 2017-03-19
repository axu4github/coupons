# -*- coding:utf-8 -*-

"""
单元测试

"""

from django.test import TestCase
from django.conf import settings


class EnvTest(TestCase):

    def test_load_custom_settings(self):
        """
        测试修改了配置文件目录（由默认创建的'${BASE_DIR}/coupons'修改为${BASE_DIR}/'configs'）是否可以顺利加载配置
        """

        import os
        self.assertIsNotNone(settings.SECRET_KEY)
        self.assertEqual(settings.BASE_DIR, os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))))
