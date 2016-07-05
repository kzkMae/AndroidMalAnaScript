# coding:utf-8

# Jsonファイルを解析

import json
import argparse

#自作のファイルをインポート
from CheckArgument import *
from FindJson import *

#引数や-hのオプションを定義
parser = argparse.ArgumentParser(prog='Jsonファイルを解析',description='オプションと引数の説明',
                                epilog='以上')
parser.add_argument('-v','--version', action='version', version='%(prog)s version')
parser.add_argument('JsonsPath',type=str, help='Jsonファイルがあるフォルダのパスを指定, 型：%(type)s，String')

arguMain = parser.parse_args()

#引数のチェック
checkNumber = argumentCheck(arguMain)
#エラーチェック
deadErrorEnd(checkNumber)

#フォルダパス
folderPath = arguMain.JsonsPath

#Jsonファイルのリストを取得
checkNumber, jsonList, jsonListSize = getJsonfileList(folderPath)

print jsonList
print jsonListSize

