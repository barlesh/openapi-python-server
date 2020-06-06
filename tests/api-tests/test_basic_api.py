# import sdk.rest.out.python.openapi_client

from __future__ import print_function
import os
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

import pytest

# enviorment
tested_host = os.environ.get("HOST", 'localhost')
tested_port = os.environ.get("PORT", 8080)

host = "http://{host}:{port}/v2".format(host=tested_host, port=tested_port)
# Defining the host is optional and defaults to https://localhost/v2
# See configuration.py for a list of all supported configuration parameters
configuration = openapi_client.Configuration(
    host=host
)


class TestBasic:
    def test_add_n_get_all(self):
        uid = 1
        description = "basic description"
        expected = [{ "description" : description, "id" : uid }]
        # Enter a context with an instance of the API client
        with openapi_client.ApiClient(configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.BasicApi(api_client)
            # Basic | Basic object that needs to be added to the basic stuff (optional)
            body = openapi_client.Basic(id=uid, description=description)
            try:
                # Add a basic stuff
                ans = api_instance.src_basic_ctrl_basic_add_basic(body=body)
            except ApiException as e:
                pass
                print("Exception when calling BasicApi->src_basic_ctrl_basic_add_basic: %s\n" % e)

            ret = api_instance.src_basic_ctrl_basic_get_all()
            print("ret:" + str(ret))
            print("expected:" + str(expected))
            assert isinstance(ret, list)
            assert isinstance(ret[0], dict)
            assert ret == expected
            # self.assertDictEqual(ret, expected)




