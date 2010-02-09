#!/usr/bin/env python
import os, sys
VERSION = (0,9,6)

def get_version():
    strversion = [str(x) for x in VERSION]
    return '.'.join(strversion)

class NotFoundError(RuntimeError):
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
        confirm("Tests had errors.")

def check_for_todos():
    result = os.system("git grep -I -ni '#[ \t]*todo'")
    if result == 0:
        confirm("There are TODO statements.")
        
def confirm(question_str):
    print ("%s Continue with commit? [y/N] " % question_str), 
    c = sys.stdin.readline()
    c = c.strip()
    if c.lower() != 'y':
        print "aborting . . . "
        exit()
    
    
        
