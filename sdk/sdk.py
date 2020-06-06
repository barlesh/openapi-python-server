import openapi_client
from openapi_client.rest import ApiException


class SDK:

    def __init__(self, host, port):
        host = "http://{host}:{port}/v2".format(host=host, port=port)
        # Defining the host is optional and defaults to https://localhost/v2
        # See configuration.py for a list of all supported configuration parameters
        self.configuration = openapi_client.Configuration(
            host=host
        )

    def addBasic(self, description,id):
        with openapi_client.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.BasicApi(api_client)
            # Basic | Basic object that needs to be added to the basic stuff (optional)
            body = openapi_client.Basic(id=id, description=description)
            try:
                # Add a basic stuff
                ans = api_instance.src_basic_ctrl_basic_add_basic(body=body)
                return ans 
            except ApiException as e:
                pass
                print("Exception when calling BasicApi->src_basic_ctrl_basic_add_basic: %s\n" % e)

    def getAll(self):
        with openapi_client.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            api_instance = openapi_client.BasicApi(api_client)

            try:
                # Add a basic stuff
                ret = api_instance.src_basic_ctrl_basic_get_all()
                return ret 
            except ApiException as e:
                pass
                print("Exception when calling BasicApi->src_basic_ctrl_basic_get_all: %s\n" % e)