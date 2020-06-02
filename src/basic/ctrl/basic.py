import json
from src.basic.bl import basic

def addBasic(body):
    try:
        d = json.loads(body)
        ret = basic.addBasic(d)
        return ret, 202
    except:
        return "error", 400