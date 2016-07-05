# coding:utf-8

import json

#結果をJsonファイル形式で保存
def saveJsonFile(jsonData,urlData, Savepath):
    #fname = Savepath + '/Result_' + urlData.split("//",1)[1] + '.json'
    fname = Savepath + '/Result_' + urlData + '.json'
    jsonFormData = json.loads(jsonData)
    with open(fname, 'w') as f:
        json.dump(jsonFormData,f,indent=4)
    return 0


