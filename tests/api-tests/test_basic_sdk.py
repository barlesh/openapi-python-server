# import sdk.rest.out.python.openapi_client

import os
# from basicSDK import sdk
import basicSDK

import pytest

# enviorment
tested_host = os.environ.get("HOST", 'localhost')
tested_port = os.environ.get("PORT", 8080)



class TestBasic:
    def test_add_n_get_all(self):
        uid = 1
        description = "basic description"
        expected = [{ "description" : description, "id" : uid }]

        testedSDK = sdk(tested_host, tested_port)
        testedSDK.addBasic(id=uid, description=description)

        ret = testedSDK.getAll()
        assert ret == expected



