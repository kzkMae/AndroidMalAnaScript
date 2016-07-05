#coding:utf-8
import glob
#Jsonファイルのリスト作成

#フォルダ内にjsonファイルがあるか否かを確認
def jsonFileExist(listSize):
    if listSize == 0:
        #jsonファイルが１つも存在しない
        print 'jsonファイルが１つもないんだゾ☆'
        return 1
    #listSizeの中身があればエラーなし
    return 0



#Jsonファイルをリストで受け取る
#返却値には，Checkコード，ファイルリスト，サイズ
def getJsonfileList(folderPath):
    jsonList = glob.glob(folderPath+'*.json')
    #Listのサイズを求める
    jsonListSize = len(jsonList)
    #Listの中身があるかを確認
    checkNum = jsonFileExist(jsonListSize)
    return checkNum, jsonList, jsonListSize

