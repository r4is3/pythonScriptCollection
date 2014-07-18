#!/usr/bin/env python
# -*- coding:UTF8 -    *-

# author @r4is3 : https://twitter/r4is3
# This is snipet to send sms with REST api given by free mobile
# DO not abuse service and use for fun only


import urllib.parse, urllib.request, sys

url='https://smsapi.free-mobile.fr/sendmsg?'
user='free-ID'
key='key-given-by-free'
msg=(" ".join(sys.argv[1:]))

while len(msg) !=0:
    q=urllib.parse.urlencode({ 'user': '%s'%user, 'pass': '%s'%key, 'msg': '%s'%msg[0:139]  })
    urllib.request.urlopen(url+q)
    msg=msg[139:]
    print (msg)
