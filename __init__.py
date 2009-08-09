VERSION = (0,9,0)

def get_version():
    strversion = [str(x) for x in VERSION]
    return '.'.join(strversion)