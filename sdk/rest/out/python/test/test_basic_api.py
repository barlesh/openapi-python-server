# coding: utf-8

"""
    My flask

    My simple flask application service  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: barlesh8@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.basic_api import BasicApi  # noqa: E501
from openapi_client.rest import ApiException


class TestBasicApi(unittest.TestCase):
    """BasicApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.basic_api.BasicApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_src_basic_ctrl_basic_add_basic(self):
        """Test case for src_basic_ctrl_basic_add_basic

        Add a basic stuff  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()