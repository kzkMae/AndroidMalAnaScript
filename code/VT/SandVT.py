#coding:utf-8
import urllib
import urllib2


#VirusTotalへURL情報をぶん投げる


def sandURLtoTV(url, urlValue,vtApikey):
    sendParas = {"url": urlValue,
                 "apikey": vtApikey}
    #エンコード
    edata = urllib.urlencode(sendParas)
    #送信
    requestData = urllib2.Request(url,edata)
    response = urllib2.urlopen(requestData)
    jsons = response.read()
    return jsons