#!/usr/bin/python36

import subprocess as sp
import os
import cgi

print("content-type: text/html")
print()


print("""
<form action='http://192.168.43.171/cgi-bin/package.py'/>
Enter your software name:
<input name='s_name'/>
</br>
""")

data=cgi.FieldStorage() #alotts mydata variable to the cgi variable
s_name=data.getvalue("s_name")

cmd='sudo ansible localhost -m package -a "name={} state=present"'.format(s_name)
print()
x=sp.getoutput(cmd)
print(x)
