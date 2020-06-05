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
    api_instance = openapi_client.BasicApi(api_client)
    body = openapi_client.Basic(id=1, description="whattt") # Basic | Basic object that needs to be added to the basic stuff (optional)
    try:
        # Add a basic stuff
        ans = api_instance.src_basic_ctrl_basic_add_basic(body=body)
    except ApiException as e:
        pass
        print("Exception when calling BasicApi->src_basic_ctrl_basic_add_basic: %s\n" % e)
    


