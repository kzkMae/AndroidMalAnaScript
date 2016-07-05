# coding:utf-8

#CSVファイルにあるURLsをVirustotalに投げるプログラム

import urllib
import urllib2
import argparse
import json

#自作のファイルをインポート
from Check.End import *
from Check.DeadEnd import *
from ReadCSVFile.ReadURLinCSVfile import *

#引数や-hのオプションを定義
parser = argparse.ArgumentParser(prog='Scan urls by VirusTotal',description='オプションと引数の説明',
                                epilog='以上')
parser.add_argument('-v','--version', action='version', version='%(prog)s version')
parser.add_argument('VTapikey',type=str, help='手前のVirusTotalのAPIkeyを入力しろやい！, 型：%(type)s，String')
parser.add_argument('CsvFile',type=str, help='URLsを記録されたCSVファイルを指定してネ, 型：%(type)s，String')

arguMain = parser.parse_args()

#引数チェック
checkNumber = argumentCheck(arguMain)
#エラーチェック
deadErrorEnd(checkNumber)

#引数を取り出す
#csvファイル
csvFPath = arguMain.CsvFile

#csvファイルからUrlを取り出す（リスト形式）
urlsData = readURLlist(csvFPath)

#scan用のVirustotalのサイト
url = "https://www.virustotal.com/vtapi/v2/url/scan"

#VirusTotalのAPIキーを指定
apikey = arguMain.VTapikey


parameters = {"url":"http://www.virustotal.com",
              "apikey": apikey}


for urlRow in urlsData:
    print urlRow[0]
    urlV = urlRow[0]
    sendParas ={"url": urlV,
                "apikey": apikey}
    #エンコード
    edata = urllib.urlencode(sendParas)
    #VirusTotalに送信
    requestData = urllib2.Request(url,edata)
    response =urllib2.urlopen(requestData)
    jsons = response.read()
    #print jsons
    #print '\n'


