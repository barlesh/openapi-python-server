import json

basic_list = [] 
def addBasic(body):
    print("addying basic")
    d = {}
    try:
        d = json.loads(body)
    except:
        print("whoops")
    basic_list.append(d)
    print("basic_object: {}".format(d))
    return d, 202