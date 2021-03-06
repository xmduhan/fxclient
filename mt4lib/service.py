# -*- coding:utf-8 -*- 

import urllib,urllib2,cookielib,json

#ckjar = cookielib.CookieJar()
#ckproc = urllib2.HTTPCookieProcessor(ckjar)
#opener = urllib2.build_opener(ckproc)
#urllib2.install_opener(opener)

try:
    from deveconfig import development
except:
    development = False

if development :
    serviceRoot = "http://192.168.0.120:8080"    
else:
    serviceRoot = "http://qisite.jios.org:11000/fxserver"   


def expertRegister(expertCode,loginId,companyName,serverName):
    try:
        data = {
            "ExpertCode":expertCode,
            "AccountLoginId":loginId,
            "AccountCompanyName":companyName,
            "AccountServerName":serverName
        }
        postData = urllib.urlencode(data)
        #url = "http://qisite.jios.org:11000/fxserver/experts/service/ExpertRegister"
        #url = "http://192.168.0.120:8080/experts/service/ExpertRegister"
        url = serviceRoot + "/experts/service/ExpertRegister"
        req = urllib2.Request(url, postData)
        response = urllib2.urlopen(req)
        content = response.read()
        return  str(json.loads(content))
    except Exception as e:
        #print(Exception,e)
        return u"{'errcode':-1,'errmsg':'fail to connect server'}"
    
    
def expertUnregister(expertInstanceId,token):
    try:
        data = {
            "ExpertInstanceId":expertInstanceId,
            "Token":token
        }
        postData = urllib.urlencode(data)
        #url = "http://qisite.jios.org:11000/fxserver/experts/service/ExpertUnregister"
        #url = "http://192.168.0.120:8080/experts/service/ExpertUnregister"
        url = serviceRoot + "/experts/service/ExpertUnregister"
        req = urllib2.Request(url, postData)
        response = urllib2.urlopen(req)
        content = response.read()
        return  str(json.loads(content))
    except Exception as e :
        #print(Exception,e)
        return u"{'errcode':-1,'errmsg':'fail to connect server'}"


        
        
