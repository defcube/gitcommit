#!/usr/bin/env python
import os

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
        print 'not found'
        return
    result = os.system(managepy + " test")
    if result != 0:
        raise TestsFailedError

if __name__ == '__main__':
    try:
        run_tests()
    except TestsFailedError:
        exit()
    os.system("git commit -a -v")    
    
        
