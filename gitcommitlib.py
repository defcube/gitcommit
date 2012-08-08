#!/usr/bin/env python
import os, sys, subprocess
VERSION = (0,9,9)

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


def remove_ignored_todos(output):
    try:
        ignores = file('.gitcommitignore', 'r').readlines()
    except IOError:
        return output
    ignores = [x.strip() for x in ignores]
    def filterme(line):
        for i in ignores:
            if line.startswith(i):
                return False
        return True
    return filter(filterme, output)


def check_for_todos():
    try:
        output = subprocess.check_output(['git', 'grep', '-I',
                                          '-ni', '#[ \t]*todo']).splitlines()
    except subprocess.CalledProcessError, e:
        output = e.output.splitlines()
    output = remove_ignored_todos(output)
    if len(output):
        print '\n'.join(output)
        confirm("There are TODO statements.")


def confirm(question_str):
    print ("%s Continue with commit? [y/N] " % question_str),
    c = sys.stdin.readline()
    c = c.strip()
    if c.lower() != 'y':
        print "aborting . . . "
        exit()