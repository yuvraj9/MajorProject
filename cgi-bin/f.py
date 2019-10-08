#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")
print()

#form=cgi.FieldStorage()
cmd="sudo docker ps -a"
x=sp.getoutput(cmd)
print(x)
