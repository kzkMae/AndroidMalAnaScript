# coding:utf-8

import os.path


#CSVファイルがあるかどうかをチェック
def isCsvfile(csvFile):
    checkNum = 0
    if not (os.path.isfile(csvFile)):
        print "んなファイルねえよ(# ﾟДﾟ)"
        checkNum = 1
    return checkNum

#拡張子がCSVで終わっているかをチェック
def extCsvfile(csvFile):
    checkNum =0
    fileName, ext = os.path.splitext(csvFile)
    if ext != '.csv':
        print "csvファイルを指定して？"
        checkNum = 1
    return checkNum

#引数をチェック
def argumentCheck(arguMain):
    checkNum = 0
    checkNum += extCsvfile(arguMain.CsvFile)
    checkNum += isCsvfile(arguMain.CsvFile)
    return checkNum

def checkURLNumber(urlsN, arguNum):
    if urlsN > arguNum:
        return 0
    return 1