# openapi_client.BasicApi

All URIs are relative to *https://localhost/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**src_basic_ctrl_basic_add_basic**](BasicApi.md#src_basic_ctrl_basic_add_basic) | **POST** /basic | Add a basic stuff


# **src_basic_ctrl_basic_add_basic**
> src_basic_ctrl_basic_add_basic(body=body)

Add a basic stuff

### Example

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://localhost/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://localhost/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.BasicApi(api_client)
    body = openapi_client.Basic() # Basic | Basic object that needs to be added to the basic stuff (optional)

    try:
        # Add a basic stuff
        api_instance.src_basic_ctrl_basic_add_basic(body=body)
    except ApiException as e:
        print("Exception when calling BasicApi->src_basic_ctrl_basic_add_basic: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Basic**](Basic.md)| Basic object that needs to be added to the basic stuff | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Nice one |  -  |
**405** | Invalid input |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

