# coding:utf-8

import os.path

#エラーチェック用関数
def x():
    return 0


#CSVファイルがあるかどうかをチェック
def isCsvfile():
    return 0

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
    return checkNum