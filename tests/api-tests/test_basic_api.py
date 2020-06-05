# import sdk.rest.out.python.openapi_client

from __future__ import print_function

import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8080/v2"
)



# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    print("1")
    api_instance = openapi_client.BasicApi(api_client)
    print("2 - api_instance: " + str(api_instance))
    body = openapi_client.Basic() # Basic | Basic object that needs to be added to the basic stuff (optional)
    print("3 - body: " + str(body))
    try:
        # Add a basic stuff
        ans = api_instance.src_basic_ctrl_basic_add_basic(body=body)
        print("4")
        print("ans: " + str(ans))
    except ApiException as e:
        pass
        print("Exception when calling BasicApi->src_basic_ctrl_basic_add_basic: %s\n" % e)
    


