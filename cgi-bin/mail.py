#!/usr/bin/python36

import subprocess as sp
import os
import cgi

print("content-type: text/html")
print()


print("""
<form action='http://192.168.43.171/cgi-bin/mail.py'/>
Enter E-mail id:
<input name='eid'/>
</br>
Enter your Password:
<input type='password' name='pas'/>
</br>
To:
<input name='to'/>
</br>
Subject:
<input name='sub'/>
</br>
Body:
<input name='body'/>
</br>
<input type='submit'>Send</input>
</br>
""")

data=cgi.FieldStorage() #alotts mydata variable to the cgi variable
eid=data.getvalue("eid")
pas=data.getvalue("pas")
to=data.getvalue("to")
sub=data.getvalue("sub")
body=data.getvalue("body")

k=sp.getstatusoutput("sudo ansible-playbook playbooks/mail.yml --extra-vars 'v={} w={} x={} y={} z={}'".format(eid,pas,to,sub,body))
print(k)
if(k[0]==0):
        print("<h1> Mail has been sent successfully</h1>")
else:
        print("<h1> Unsucessfull</h1>")
