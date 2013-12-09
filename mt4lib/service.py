# -*- coding:utf-8 -*- 

import urllib,urllib2,cookielib,json

#ckjar = cookielib.CookieJar()
#ckproc = urllib2.HTTPCookieProcessor(ckjar)
#opener = urllib2.build_opener(ckproc)
#urllib2.install_opener(opener)

def expertRegister(expertCode,loginId,companyName,serverName):
    try:
        data = {
            "ExpertCode":expertCode,
            "AccountLoginId":loginId,
            "AccountCompanyName":companyName,
            "AccountServerName":serverName
        }
        postData = urllib.urlencode(data)
        url = "http://qisite.jios.org:11000/fxserver/experts/service/ExpertRegister"
        #url = "http://192.168.0.120:8080/experts/service/ExpertRegister"
        req = urllib2.Request(url, postData)
        response = urllib2.urlopen(req)
        content = response.read()
        return  str(json.loads(content))
    except:
        return u"{'errcode':-1,'errmsg':'fail to connect server'}"
    
    



        
        
