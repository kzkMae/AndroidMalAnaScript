# coding:utf-8

#CSVファイルにあるURLsをVirustotalに投げるプログラム

import argparse
import os.path

#自作のファイルをインポート
from Check.End import *
from Check.DeadEnd import *
from ReadCSVFile.ReadURLinCSVfile import *
from VT.SandVT import *
from saveResultJson.VTresultJson import *

#引数や-hのオプションを定義
parser = argparse.ArgumentParser(prog='Scan urls by VirusTotal',description='オプションと引数の説明',
                                epilog='以上')
parser.add_argument('-v','--version', action='version', version='%(prog)s version')
parser.add_argument('VTapikey',type=str, help='手前のVirusTotalのAPIkeyを入力しろやい！, 型：%(type)s，String')
parser.add_argument('CsvFile',type=str, help='URLsを記録されたCSVファイルを指定してネ, 型：%(type)s，String')
parser.add_argument('urlNumber',type=int, help='結果が欲しいものを選んでね\r\n'
                                               '1:スキャン依頼\r\n'
                                               '2:レポート取得, 型：%(type)s，Integer')

arguMain = parser.parse_args()


#引数チェック
checkNumber = argumentCheck(arguMain)
#エラーチェック
deadErrorEnd(checkNumber)

#引数を取り出す
#csvファイル
csvFPath = arguMain.CsvFile
#CSVファイルのあるDir名を取得
savePath = os.path.dirname(csvFPath)

#csvファイルからUrlを取り出す（リスト形式）
urlsData = readURLlist(csvFPath)

#scan用のVirustotalのサイト
url = ["https://www.virustotal.com/vtapi/v2/url/scan",
       "http://www.virustotal.com/vtapi/v2/url/report"]

#URLの数を取得
uNumber = arguMain.urlNumber
urlNumber = len(url)
checkNumber = checkURLNumber(urlNumber,uNumber)
#エラーチェック
deadErrorEnd(checkNumber)

#VirusTotalのAPIキーを指定
apikey = arguMain.VTapikey


parameters = {"url":"http://www.virustotal.com",
              "apikey": apikey}

#カウンタ
i = 0

for urlRow in urlsData:
    i = stopSendtoVT(i)
    print urlRow[0]
    urlV = urlRow[0]
    #Json形式で受け取り
    #for j in range(urlNumber):
    jsonsData = sandURLtoTV(url[uNumber],urlV, apikey, uNumber)
    #print jsons
    saveJsonFile(jsonsData, urlV, savePath)
    #print '\n'

print '無問題だゾ☆'
