# coding:utf-8

#CSVファイルにあるURLsをVirustotalに投げるプログラム

import urllib
import urllib2
import argparse

#自作のファイルをインポート
from Check.End import *

#引数や-hのオプションを定義
parser = argparse.ArgumentParser(prog='Scan urls by VirusTotal',description='オプションと引数の説明',
                                epilog='以上')
parser.add_argument('-v','--version', action='version', version='%(prog)s version')
parser.add_argument('VTapikey',type=str, help='手前のVirusTotalのAPIkeyを入力しろやい！, 型：%(type)s，String')
parser.add_argument('CsvFile',type=str, help='URLsを記録されたCSVファイルを指定してネ, 型：%(type)s，String')

arguMain = parser.parse_args()



#scan用のVirustotalのサイト
url = "https://www.virustotal.com/vtapi/v2/url/scan"

apikey =

parameters = {"url":"http://www.virustotal.com",
              "apikey": apikey}