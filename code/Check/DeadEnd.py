# coding:utf-8

import sys

#強制終了用の関数

def x():
    return 0


def deadErrorEnd(checkNumber):
    if not (checkNumber == 0):
        print "終了します"
        sys.exit()
    return 0