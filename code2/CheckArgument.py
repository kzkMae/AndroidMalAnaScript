#coding:utf-8

import sys
import os.path

#強制終了用の関数


def deadErrorEnd(checkNumber):
    if not (checkNumber == 0):
        print "終了します"
        sys.exit()
    return 0

def isPath(path):
    if not (os.path.isdir(path)):
        print "そんなフォルダはないですよ"
        return 1
    return 0


def argumentCheck(argument):
    checkNum =0
    checkNum += isPath(argument.JsonsPath)
    return checkNum