# -*- coding:utf-8 -*- 

def read(file,var):        
    try:
        lc = {}
        execfile(file,lc)
        config = lc["config"]
        str = "config['%s']" % "']['".join(var.split("\\"))
        result = eval(str)
    except:
        result = None
    return result

''' a code for testing 
file = "I:\\Program Files\\HotForex MetaTrader\\experts\\config\\pycfg\\Scalping.py"
var = "HF Markets Ltd\\Micro\\EURCAD\\bands_period"
value = read(file,var)
print(value)
'''




        
        
