#coding:utf-8

import json

#使用するキーを定義
detectionB = 'positives'

def detectionCheck(JsonFile):
    #初期値
    detectionNum = 0
    detection = 0
    #fname = ''

    #Jsonファイルを開く
    f = open(JsonFile, 'r')
    jsonData = json.load(f)
    if jsonData[detectionB] > 0:
        detection += 1
        detectionNum = jsonData[detectionB]
        #fname = JsonFile
    #Jsonファイルを閉じる
    f.close()
    return detection, detectionNum
