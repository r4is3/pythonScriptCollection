#!/usr/bin/env python3
# -*- coding:UTF8 -    *-

# author @r4is3 : https://twitter/urkraftv
# This is snipet to send sms with REST api given by free mobile
# DO not abuse service and use for fun only


import urllib.parse, urllib.request, sys, json


def sendSms(*message):
    url='https://smsapi.free-mobile.fr/sendmsg?'
    user='<USER>'
    key='<KEY>'
    msg=(" ".join(message[0][0:]))

    while len(msg) !=0:
    	q=urllib.parse.urlencode({ 'user': '%s'%user, 'pass': '%s'%key, 'msg': '%s'%msg[0:139]  })
    	urllib.request.urlopen(url+q)
    	msg=msg[139:]
    	print (msg)


url='https://www.bitstamp.net/api/v2/ticker/'
arg=(sys.argv[1:])
print(arg[0])


#q=urllib.parse.urlencode({arg[0]})
print ('%s'%url,'%s'%arg[0])
request=urllib.request.urlopen(url+arg[0])
str=request.read().decode('utf-8')
jsonObj=json.loads(str)
print ('Highest rate :'+jsonObj['high'])
print ('Latest rate :'+jsonObj['last'])

latestRate=float(jsonObj['last'])

# Change rate to add you own alert
rate2buy=float(50)
if latestRate < rate2buy:
#  print (latestRate)
  msg2send='This is the latest rate of LTC : %d, check if you want to buy it'%latestRate
  sendSms(msg2send.split())
