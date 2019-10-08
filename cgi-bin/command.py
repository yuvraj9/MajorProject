#!/usr/bin/python36

import subprocess as sp
import os
import cgi

print("content-type: text/html")
print()

print("""
<form action='http://192.168.43.171/cgi-bin/command.py'/>
Enter the command you want to run:
<input name='command'/>
</br>
""")

data=cgi.FieldStorage() #alotts mydata variable to the cgi variable
command=data.getvalue("command")

cmd='sudo {}'.format(command)
x=sp.getoutput(cmd)
print('\n')
print(x)
