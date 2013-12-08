# -*- coding:utf-8 -*- 

def readFile(file):
    try:
        g = {}
        execfile(file,g)        
        result = unicode(g["config"])
    except:
        result = unicode({})
    return result


def printTrue(step):
    try:
        print(step,"True=",True)
    except:
        print(step,"True=",None)

def readDictValue(dictStr,path):
    try:        
        config = eval(dictStr)
        result = eval("config['%s']" % "']['".join(path.split("/")))
    except Exception as e:
        result = None
    return result

def readDictValueStr(dictStr,path):
    try:
        result = unicode(readDictValue(dictStr,path))
    except:
        result = "None"
    return result
          
def readDictValueType(dictStr,path):
    try:        
        result = unicode(type(readDictValue(dictStr,path)))
    except:
        result = "NoneType"
    return result


'''
def ReadFile(file):
    try:
        g = {}
        execfile(file,g)
        code = "g['%s']" % "']['".join(var.split("/"))
        result = eval(code)  
    except:
        result = None
    return result
'''


''' a code for testing 
file = "I:\\Program Files\\HotForex MetaTrader\\experts\\config\\pycfg\\Scalping.py"
var = "HF Markets Ltd/Micro/EURCAD/bands_period"
value = read(file,var)
print(value)
'''




        
        
