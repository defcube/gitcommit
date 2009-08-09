#!/usr/bin/env python
import os
VERSION = (0,9,0)

def get_version():
    strversion = [str(x) for x in VERSION]
    return '.'.join(strversion)

class NotFoundError(RuntimeError):
    pass

class TestsFailedError(RuntimeError):
    pass

def find_managepy():
    curpath = os.getcwd()
    while True:
        curdirlist = os.listdir(curpath)
        if 'manage.py' in curdirlist:
            return curpath + '/manage.py'
        if '.git' in curdirlist:
            raise NotFoundError
        curpath, tail = os.path.split(curpath)
        if tail == '':
            raise NotFoundError
        
def run_tests():
    try:
        managepy = find_managepy()
    except NotFoundError:
        return
    result = os.system(managepy + " test")
    if result != 0:
        raise TestsFailedError

    
        
