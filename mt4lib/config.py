# -*- coding:utf-8 -*- 

def read(file,var):
    try:
        lc = {}
        execfile(file,lc)
        config = lc["config"]
        code = "config['%s']" % "']['".join(var.split("\\"))
        result = eval(code)  
    except:
        result = None
    return result


def test(file,var):   
    return file


''' a code for testing 
file = "I:\\Program Files\\HotForex MetaTrader\\experts\\config\\pycfg\\Scalping.py"
var = "HF Markets Ltd\\Micro\\EURCAD\\bands_period"
value = read(file,var)
print(value)
'''




        
        
