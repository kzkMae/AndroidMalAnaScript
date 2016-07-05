# coding:utf-8

import csv

#csvファイルからURLを読みだす

def readURLlist(csvFile):
    #空リストの作成
    urlList = []
    #Csvファイルの読み出し
    f = open(csvFile,'rb')
    urldata = csv.reader(f)

    #URLのリストを取得（別のリストに書き込む）
    for row in urldata:
        urlList.append(row)


    return urlList