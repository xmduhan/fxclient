# -*- coding:utf-8 -*- 

def ReadValue(file,var):
    try:
        g = {}
        execfile(file,g)
        code = "g['%s']" % "']['".join(var.split("/"))
        result = eval(code)  
    except:
        result = None
    return result

''' a code for testing 
file = "I:\\Program Files\\HotForex MetaTrader\\experts\\config\\pycfg\\Scalping.py"
var = "HF Markets Ltd/Micro/EURCAD/bands_period"
value = read(file,var)
print(value)
'''




        
        
