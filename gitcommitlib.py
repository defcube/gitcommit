#!/usr/bin/env python
import os, sys
VERSION = (0,9,1)

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

def check_for_todos():
    result = os.system("git grep -ni '#[ \t]*todo'")
    if result == 0:
        print "There are TODO statements. Continue with commit? [y/N] ",
        c = sys.stdin.read(1)
        if c.lower() != 'y':
            print "aborting . . . "
            exit()

if __name__ == '__main__':
    try:
        run_tests()
    except TestsFailedError:
        exit()
    check_for_todos()
    os.system("git commit -a -v")    
    
        
