#!/usr/bin/python36

import subprocess as sp
import cgi

print("content-type: text/html")

form=cgi.FieldStorage()
cname=form.getvalue("s")
cmd="sudo docker start {}".format(cname)
x=sp.getoutput(cmd)
print("location: http://192.168.43.171/cgi-bin/run.py")
print()
