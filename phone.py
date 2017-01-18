#coding utf-8

from androidhelper import sl4a
import time

print "hello"
# droid.smsSend("18380434045","sms")
droid = sl4a.Android()

def findKeyWord():
    keywordList = {"appmonitor", "analysis"}
    listIds = droid.smsGetMessageIds(True)

    for id in listIds[1]:
        sms = droid.smsGetMessageById(id)
        smsstring = str(sms[1])
        for keyword in keywordList:
            num = smsstring.find(keyword)
            if num > 0:
                print "find keyword:" + keyword
                return id
    return -1

def isSmsReaded(id):
    sms = droid.smsGetMessageById(id)
    smsd = sms[1]
    print smsd['read']
    print type(smsd['read'])
    if smsd['read'] == '0':
        return False
    else:
        return True

def checkSms(id):
    while True:
        if isSmsReaded(id):
            break
        droid.vibrate(600)
        time.sleep(3)

while True:

    id = findKeyWord()
    print id
    if id != -1:
        checkSms(id)
    time.sleep(10)







