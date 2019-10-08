#!/usr/bin/python36
import subprocess as sp
import cgi

print("content-type: text/html\n")

x=5
#print(x)
#print(sp.getoutput("date"))
#print(sp.getoutput("id"))

mydata=cgi.FieldStorage() #alotts mydata variable to the cgi variable
y=mydata.getvalue("q")

print(y)
print(sp.getoutput("sudo " + y))
