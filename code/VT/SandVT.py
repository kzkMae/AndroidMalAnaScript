#coding:utf-8
import urllib
import urllib2
import time

#VirusTotalへURL情報をぶん投げる


def sandURLtoTV(url, urlValue,vtApikey, getType):
    sendParaTypes = [{"url": urlValue,
                 "apikey": vtApikey},
                 {"resource":urlValue,
                  "apikey": vtApikey}]
    sendParas = sendParaTypes[getType]
    #エンコード
    edata = urllib.urlencode(sendParas)
    #送信
    requestData = urllib2.Request(url,edata)
    response = urllib2.urlopen(requestData)
    jsons = response.read()
    return jsons


#フリーのAPIキーの場合の１分間に送ることができる数
limitVT = 4

#VirusTotal４つスキャンするごとに１分（事実上90秒）停止
def stopSendtoVT(count):
    if count >= limitVT:
        time.sleep(90)
        return 1
    count += 1
    return count