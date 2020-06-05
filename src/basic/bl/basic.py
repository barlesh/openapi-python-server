
basic_list = [] 

def addBasic(basicObj):
    print("addying basic")
    basic_list.append(basicObj)
    print("basic_object: {}".format(basicObj))
    return basicObj

def getAll():
    return basic_list