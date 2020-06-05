import json
from src.basic.bl import basic

def addBasic(body):
    try:
        d = json.loads(body)
        ret = basic.addBasic(d)
        return ret, 202
    except:
        return "error", 400

def getAll():
    try:
        ret = basic.getAll()
        return ret, 200
    except:
        return "error", 400